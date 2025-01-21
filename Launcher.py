# -*- coding: utf-8 -*-
"""
Create on Mon 1月 20 09:29:56 2025
@author: fangg
"""
import tkinter as tk
from tkinter import messagebox, ttk
import os
import base64
import subprocess

def get_users():
    users_dict = {}
    users_list = os.listdir("Users")
    for i in range(len(users_list)):
        with open("Users/" + users_list[i] + "/password.dat", "rb") as f:
            users_dict[users_list[i]] = f.read()
    return users_dict

def log_in(username, password):
    global users, usernameEntry, usernames
    if username == "注册一个新用户":
        subprocess.Popen(["python", "Register.py"])
        root.destroy()
        return
    if username in users and users[username] == base64.b64encode(password):
        messagebox.showinfo("登录成功", "欢迎使用BGGame!")
        subprocess.Popen(['python', 'Main.py', "logen", username])
        root.destroy()
    else:
        messagebox.showinfo("登录失败", "用户名或密码不匹配")

root = tk.Tk()
root.title('登录')
root.geometry("350x120")
root.config(bg="white")

try:
    os.mkdir("Users")
except FileExistsError:
    pass
users = get_users()
usernames = []
for i in users.keys():
    usernames.append(i)
usernames.append("注册一个新用户")

style = ttk.Style()
style.configure("TButton", bg="white", font=("Microsoft YaHei", 13))

tipLabel = tk.Label(root, text="   用户名：\n      密码：", font=("Microsoft YaHei", 15), bg="white")
tipLabel.place(x=10, y=10)

usernameEntry = ttk.Combobox(root, font=("Microsoft YaHei", 12), width=18, value=usernames)
usernameEntry.current(0)
usernameEntry.place(x=120, y=10)

passwordEntry = ttk.Entry(root, show="*", font=("Microsoft YaHei", 12))
passwordEntry.place(x=120, y=40)

registerButton = ttk.Button(root, text="登录", command=lambda: log_in(usernameEntry.get(), passwordEntry.get().encode("utf-8")))
registerButton.place(x=120, y=70)

root.mainloop()