import tkinter as tk
from tkinter import filedialog, messagebox
import os
import random

# Globals
otp = None
current_user = {}

# Dummy users
users_db = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
}

# GUI Setup
root = tk.Tk()
root.title("🔐 Secure File Manager")
root.geometry("600x450")

# ---------- Authentication ----------

def login():
    username = username_entry.get().lower()
    password = password_entry.get()

    if username in users_db and users_db[username]["password"] == password:
        global current_user
        current_user = {"username": username, "role": users_db[username]["role"]}
        messagebox.showinfo("Login", f"Welcome {username.capitalize()}! Role: {current_user['role']}")
        login_frame.pack_forget()
        otp_frame.pack()
        generate_otp()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# ---------- OTP ----------
def generate_otp():
    global otp
    otp = random.randint(100000, 999999)
    messagebox.showinfo("OTP", f"Your OTP is: {otp}")

def verify_otp():
    if otp_entry.get() == str(otp):
        messagebox.showinfo("Success", "OTP Verified!")
        otp_frame.pack_forget()
        main_menu.pack()
    else:
        messagebox.showerror("Failed", "Invalid OTP!")

# ---------- Access Control ----------
def check_access(operation):
    if current_user["role"] == "admin" or (current_user["role"] == "user" and operation == "read"):
        return True
    else:
        messagebox.showwarning("Access Denied", f"'{current_user['role']}' cannot perform '{operation}' operation.")
        return False

# ---------- File Operations ----------
def write_file():
    if not check_access("write"):
        return
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    if filename:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(file_content.get("1.0", tk.END))
        messagebox.showinfo("File", "File written successfully.")

def read_file():
    if not check_access("read"):
        return
    filename = filedialog.askopenfilename()
    if filename:
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        file_content.delete("1.0", tk.END)
        file_content.insert(tk.END, content)

def rename_file():
    if not check_access("rename"):
        return
    old = filedialog.askopenfilename()
    if old:
        new = filedialog.asksaveasfilename()
        os.rename(old, new)
        messagebox.showinfo("Rename", "File renamed successfully.")

def delete_file():
    if not check_access("delete"):
        return
    filename = filedialog.askopenfilename()
    if filename:
        os.remove(filename)
        messagebox.showinfo("Delete", "File deleted successfully.")

def scan_file():
    filename = filedialog.askopenfilename()
    if filename:
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            if "malware" in content or "virus" in content:
                messagebox.showwarning("Scan", "Threat detected!")
            else:
                messagebox.showinfo("Scan", "No threats found.")

# ---------- GUI Layout ----------

# Login Frame
login_frame = tk.Frame(root)
tk.Label(login_frame, text="🔐 Login", font=("Arial", 16)).pack(pady=10)
tk.Label(login_frame, text="Username:").pack()
username_entry = tk.Entry(login_frame)
username_entry.pack()
tk.Label(login_frame, text="Password:").pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()
tk.Button(login_frame, text="Login", command=login).pack(pady=10)
login_frame.pack(pady=50)

# OTP Frame
otp_frame = tk.Frame(root)
tk.Label(otp_frame, text="Enter OTP sent to you").pack(pady=10)
otp_entry = tk.Entry(otp_frame)
otp_entry.pack()
tk.Button(otp_frame, text="Verify OTP", command=verify_otp).pack(pady=10)

# Main Menu Frame
main_menu = tk.Frame(root)
tk.Label(main_menu, text="📂 Secure File Manager", font=("Arial", 16)).pack(pady=10)
file_content = tk.Text(main_menu, height=10)
file_content.pack(pady=10)

btn_frame = tk.Frame(main_menu)
btn_frame.pack()

tk.Button(btn_frame, text="Write File", command=write_file).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Read File", command=read_file).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Rename File", command=rename_file).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Delete File", command=delete_file).grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="Scan File", command=scan_file).grid(row=0, column=4, padx=5)

# ---------- Start GUI ----------
root.mainloop()
