# -*- coding: utf-8 -*-
"""
Create on Mon 1月 19 22:28:36 2025
@author: fangg
"""
from tkinter import ttk, messagebox
import tkinter as tk
import base64
import subprocess
import os

def register_user(username, password, repassword):
    if not (16 > len(username) and not " " in username):
        messagebox.showerror("Error", "用户名过长/含有空格！")
        return
    if password != repassword:
        messagebox.showerror("Error", "输入的密码不一致！")
        return
    if not (16 > len(password) and len(password) > 4 and not " " in password):
        messagebox.showerror("Error", "密码过长/短/含有空格！")
        return
    if os.path.exists("Users/" + username):
        messagebox.showerror("Error", "该用户已存在！")
        return
    os.mkdir("Users/" + username)
    with open("Users/" + username + "/password.dat", "wb") as f:
        password = password.encode("utf-8")
        password_b64bytes = base64.b64encode(password)
        f.write(password_b64bytes)
    messagebox.showinfo("注册成功", "注册成功！")
    subprocess.Popen(["python", "Launcher.py"])
    root.destroy()


root = tk.Tk()
root.title('注册账户')
root.geometry("350x140")
root.config(bg="white")

style = ttk.Style()
style.configure("TButton", bg="white", font=("Microsoft YaHei", 13))

tipLabel = tk.Label(root, text="   用户名：\n      密码：\n再次输入：", font=("Microsoft YaHei", 15), bg="white")
tipLabel.place(x=10, y=10)

usernameEntry = ttk.Entry(root, font=("Microsoft YaHei", 12))
usernameEntry.place(x=120, y=10)

passwordEntry = ttk.Entry(root, show="*", font=("Microsoft YaHei", 12))
passwordEntry.place(x=120, y=40)

repasswordEntry = ttk.Entry(root, show="*", font=("Microsoft YaHei", 12))
repasswordEntry.place(x=120, y=70)

registerButton = ttk.Button(root, text="注册", command=lambda:
                 register_user(usernameEntry.get(), passwordEntry.get(), repasswordEntry.get()))
registerButton.place(x=120, y=100)

root.mainloop()