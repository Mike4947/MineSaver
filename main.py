import os
import shutil
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QLabel, \
    QCheckBox, QFormLayout, QMessageBox, QScrollArea, QGroupBox, QProgressBar
from PyQt5.QtCore import Qt

# Define app memory file
memory_file = "backup_memory.json"


# Check if there's a saved memory (last used location)
def load_memory():
    if os.path.exists(memory_file):
        with open(memory_file, "r") as f:
            return json.load(f)
    # Default Minecraft world path
    default_world_path = os.path.expanduser(r"~\AppData\Roaming\.minecraft\saves")
    return {"last_backup": "", "world_path": default_world_path}


# Save app memory (last used location)
def save_memory(path, world_path):
    with open(memory_file, "w") as f:
        json.dump({"last_backup": path, "world_path": world_path}, f)


# Get the list of Minecraft worlds from the world path
def get_minecraft_worlds(world_path):
    if not os.path.exists(world_path):
        return []
    return [world for world in os.listdir(world_path) if os.path.isdir(os.path.join(world_path, world))]


# Backup Minecraft world
def backup_world(world_paths, backup_location, progress_bar):
    # Create backup folder if not exists
    backup_folder = os.path.join(backup_location, "Minecraft_Backups")
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    # Copy selected worlds to the backup location
    total_worlds = len(world_paths)
    progress_bar.setMaximum(total_worlds)

    for idx, world_path in enumerate(world_paths):
        world_name = os.path.basename(world_path)
        backup_path = os.path.join(backup_folder, f"{world_name}_backup")
        try:
            shutil.copytree(world_path, backup_path)
            progress_bar.setValue(idx + 1)
        except Exception as e:
            QMessageBox.critical(None, "Error", f"An error occurred while backing up the world '{world_name}': {e}")
        else:
            print(f"World '{world_name}' backed up successfully!")

    save_memory(backup_location, load_memory()['world_path'])  # Save last used backup location


# Extract a backuped world to Minecraft Saves location
def extract_backup_world(backup_path, world_name, world_path):
    destination_path = os.path.join(world_path, world_name)
    if os.path.exists(destination_path):
        overwrite = QMessageBox.question(None, "Overwrite",
                                         f"The world '{world_name}' already exists. Do you want to overwrite it?",
                                         QMessageBox.Yes | QMessageBox.No)
        if overwrite == QMessageBox.No:
            return

    try:
        shutil.copytree(backup_path, destination_path)
        QMessageBox.information(None, "Success", f"World '{world_name}' has been restored to the main location.")
    except Exception as e:
        QMessageBox.critical(None, "Error", f"An error occurred while extracting the world '{world_name}': {e}")


# Export a world to the main Minecraft saves location
def export_world_to_main_location(backup_location, world_name, world_path):
    backup_folder = os.path.join(backup_location, "Minecraft_Backups")
    world_backup_path = os.path.join(backup_folder, f"{world_name}_backup")

    if not os.path.exists(world_backup_path):
        QMessageBox.critical(None, "Error", f"The world '{world_name}' does not exist in backups.")
        return

    extract_backup_world(world_backup_path, world_name, world_path)


# Main Window Class
class BackupApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Minecraft World Backup")
        self.setGeometry(100, 100, 600, 400)

        # Load previous memory
        self.memory = load_memory()
        self.last_backup = self.memory.get("last_backup")
        self.world_path = self.memory.get("world_path")

        # UI Elements
        self.layout = QVBoxLayout()

        # Info Label
        self.info_label = QLabel(f"Current World Path: {self.world_path}")
        self.layout.addWidget(self.info_label)

        # Main Buttons Layout
        self.main_buttons_layout = QHBoxLayout()

        # Backup Button
        self.backup_button = QPushButton("Backup Minecraft World")
        self.backup_button.clicked.connect(self.show_world_selection)
        self.main_buttons_layout.addWidget(self.backup_button)

        # Export Button
        self.export_button = QPushButton("Export a World to Main Location")
        self.export_button.clicked.connect(self.export_world)
        self.main_buttons_layout.addWidget(self.export_button)

        # Extract Backuped World Button
        self.extract_button = QPushButton("Extract Backuped World")
        self.extract_button.clicked.connect(self.extract_backuped_world)
        self.main_buttons_layout.addWidget(self.extract_button)

        self.layout.addLayout(self.main_buttons_layout)

        # Change Default World Path Button
        self.change_world_path_button = QPushButton("Change Default World Path")
        self.change_world_path_button.clicked.connect(self.change_world_path)
        self.layout.addWidget(self.change_world_path_button)

        # Progress Bar for Backup Process
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.layout.addWidget(self.progress_bar)

        # Quit Button
        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(self.quit_app)
        self.layout.addWidget(self.quit_button)

        # Set Layout
        self.setLayout(self.layout)

    def show_world_selection(self):
        # Get list of Minecraft worlds
        worlds = get_minecraft_worlds(self.world_path)
        if not worlds:
            QMessageBox.critical(None, "Error", "No Minecraft worlds found.")
            return

        # Create a scrollable area for checkboxes
        self.checkbox_group = QGroupBox("Select Worlds to Backup")
        scroll_layout = QFormLayout()
        self.checkboxes = []

        for world in worlds:
            checkbox = QCheckBox(world)
            scroll_layout.addWidget(checkbox)
            self.checkboxes.append(checkbox)

        self.checkbox_group.setLayout(scroll_layout)

        # Create a scrollable widget for checkboxes
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.checkbox_group)
        scroll_area.setWidgetResizable(True)

        # Show the scroll area in the main layout
        self.layout.addWidget(scroll_area)

        # Add backup action button after selecting worlds
        self.backup_selected_button = QPushButton("Backup Selected Worlds")
        self.backup_selected_button.clicked.connect(self.backup_selected_worlds)
        self.layout.addWidget(self.backup_selected_button)

    def backup_selected_worlds(self):
        # Get the selected worlds
        selected_worlds = []
        for checkbox in self.checkboxes:
            if checkbox.isChecked():
                selected_worlds.append(os.path.join(self.world_path, checkbox.text()))

        if not selected_worlds:
            QMessageBox.critical(None, "Error", "No worlds selected for backup.")
            return

        # Open dialog to choose the backup location
        backup_location = QFileDialog.getExistingDirectory(self, "Select Backup Location")
        if backup_location:
            self.progress_bar.setValue(0)  # Reset progress bar
            backup_world(selected_worlds, backup_location, self.progress_bar)

    def export_world(self):
        # Let the user choose a world from backups to export
        world_name, _ = QFileDialog.getItem(self, "Select a World to Export", "Select a World",
                                            self.get_backuped_worlds(), 0, False)
        if world_name:
            export_world_to_main_location(self.last_backup, world_name, self.world_path)

    def extract_backuped_world(self):
        # Let the user select a world from backups to extract
        world_name, _ = QFileDialog.getItem(self, "Select a World to Extract", "Select a World",
                                            self.get_backuped_worlds(), 0, False)
        if world_name:
            backup_folder = os.path.join(self.last_backup, "Minecraft_Backups")
            backup_path = os.path.join(backup_folder, f"{world_name}_backup")
            extract_backup_world(backup_path, world_name, self.world_path)

    def get_backuped_worlds(self):
        backup_folder = os.path.join(self.last_backup, "Minecraft_Backups")
        if not os.path.exists(backup_folder):
            return []
        return [world.replace("_backup", "") for world in os.listdir(backup_folder) if
                os.path.isdir(os.path.join(backup_folder, world))]

    def change_world_path(self):
        # Open dialog to choose the new Minecraft world path
        new_world_path = QFileDialog.getExistingDirectory(self, "Select Minecraft World Directory")
        if new_world_path:
            self.world_path = new_world_path
            self.info_label.setText(f"Current World Path: {self.world_path}")
            save_memory(self.last_backup, self.world_path)

    def quit_app(self):
        # Close the app
        self.close()


# Main function to run the app
def main():
    app = QApplication([])
    window = BackupApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
