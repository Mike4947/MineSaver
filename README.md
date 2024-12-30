# **Minecraft World Backup & Restore Application** 🛠️🎮

## **Overview** 📝

This Python-based application allows Minecraft players to easily **backup**, **restore**, and **manage** their Minecraft worlds. It provides a user-friendly interface built with **PyQt5**, enabling you to back up multiple Minecraft worlds, restore them, and export them to your main game folder. The application is designed to be portable, meaning you can store it on a USB key and run it on any machine without accessing the `AppData` directory.

---

⚠️ **Warning: Early Beta Version!** ⚠️

This application is currently in its **early beta** phase. While we have tested the core features, **bugs and unexpected issues** may still occur. Please use the app with caution and make sure to **back up your data** before using it.

💥 **Known issues**: Some functionality may not work as expected. 
🔧 **Bug fixes**: I am alone to make those project, so bug can be long to fix.

Thank you for your understanding and support as we continue to develop and improve the app! 🙏

---

This should clearly inform users about the app's status. Let me know if you'd like to modify anything!

## **Features** 🌟

- **Backup Minecraft Worlds** 📦: Select and back up one or multiple Minecraft worlds with ease.
- **Restore Worlds** 🔄: Extract a backed-up world back to the main Minecraft saves folder.
- **Export Worlds** 📤: Export a world from the backup folder to the main location.
- **Change World Path** 🔧: Change the default Minecraft saves location.
- **Portable** 💼: Run the app from a USB drive without requiring access to the `AppData` directory.
- **Progress Bar** 📊: Visualize backup progress with a progress bar.
- **Multi-world Selection** ✅: Choose multiple worlds to back up at once.
- **Error Handling** ⚠️: Get clear error messages when something goes wrong.

---

## **Installation** 🛠️

### **Requirements** 💻

- **Python 3.x**: Make sure you have Python 3 installed on your system.
- **PyQt5**: This application uses the **PyQt5** library for the user interface. You can install it via pip:

```bash
pip install pyqt5
```

### **Setup** ⚙️

1. **Clone the repository** or download the script file to your computer or USB drive.
   
2. **Run the application** by executing the script:

```bash
python backup_minecraft_world.py
```

---

## **Usage** 📖

### **1. Backup Minecraft Worlds** 💾

- Click the **"Backup Minecraft World"** button.
- A list of Minecraft worlds will appear. Select the worlds you want to back up and press **"Backup Selected Worlds"**.
- Choose the backup location (it will create a folder named `Minecraft_Backups`).
- Your worlds will be backed up, and the progress will be shown in the progress bar.

### **2. Export a World to the Main Location** 📤

- Click the **"Export a World to Main Location"** button.
- Select a world from the list of backed-up worlds to restore it to the main Minecraft saves folder.

### **3. Restore a World from Backup** 🔄

- Click the **"Extract Backuped World"** button.
- Choose a world from the backup folder and restore it to the main saves folder.

### **4. Change Default World Path** 🔧

- Click the **"Change Default World Path"** button.
- Choose a new directory for your Minecraft saves folder.

### **5. Quit the Application** ❌

- Simply click **"Quit"** to exit the application.

---

## **Screenshot** 📸

![image](https://github.com/user-attachments/assets/b6d62d07-6dd7-4dc6-91c2-415d37bf609c)


*Example of the Minecraft World Backup & Restore Application user interface.*

---

## **Customization** 🎨

You can customize the app by:

- Changing the default world path.
- Selecting the backup location for Minecraft worlds.
- Updating the list of worlds to backup with a simple change in the code.

---

## **Contributing** 🤝

If you'd like to contribute to the development of this app, feel free to fork the repository, make your changes, and submit a pull request. Contributions can include new features, bug fixes, and improvements.

---

## **License** 📜

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## **Contact** 📬

For questions, feedback, or suggestions, you can reach out to:

- **GitHub**: [GitHub Profile](https://github.com/Mike4947)
