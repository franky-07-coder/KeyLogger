🔑 Advanced Keylogger (Python)

This is a simple but powerful keylogger application made with Python.
It comes with a clean GUI (Tkinter), so you don’t need to touch the terminal to start or stop logging.

Every time you hit Start Logging, a fresh log file is created inside a logs/ folder, and all the keys you type are saved there.
At the same time, you can also see your keystrokes appear live in the app’s preview box.

✨ What it can do

Start and stop keylogging with just a button click.

Save all keystrokes into a timestamped log file inside the logs/ folder.

Show a live preview of what you’re typing inside the window.

Quickly open the logs folder using the “Open Logs” button.

Automatically stops when you press the Esc key.

⚙️ What you need

Python 3.8+

The pynput library (install with pip install pynput).

Tkinter (already included with Python by default).

🚀 How to use

Clone or download this project.

Install the required library:

pip install pynput


Run the script:

python keylogger.py


Use the GUI:

Click Start Logging → begins recording keystrokes.

Click Stop Logging → ends the session.

Click Open Logs → opens the folder with your saved log files.

📝 Example log file

A log file might look something like this:

a b c Key.space d e f g
Key.enter h i j

⚠️ Important note

This program is made for learning and personal use only.
Don’t run it on anyone else’s computer without their knowledge or permission.