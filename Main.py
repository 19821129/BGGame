import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import os
import random
import shutil
import sys

try:
    import subprocess
except:
    os.system('pip install subprocess')

try:
    from PIL import ImageTk, Image
except:
    os.system('pip install pillow')

gamepath = os.path.join(os.path.dirname(__file__ ) + "\\Games")

tips = [
    "点击“启动！”\n来运行游戏！",
    "点击“添加游戏”\n来添加新游戏！",
    "点击“删除游戏”\n来移除游戏！",
    "上下翻页查看\n更多游戏！"
]

tip_index = 0

themes = {
    '默认主题': {
        'bg_color': 'white',
        'fg_color': 'black',
        'font': ("Microsoft YaHei", 18),
        'button_bg': 'white',
        'button_fg': 'black',
        'images_dir': 'images2'
    },
    '多彩主题': {
        'bg_color': 'white',
        'fg_color': 'black',
        'font': ("Microsoft YaHei", 18),
        'button_bg': 'white',
        'button_fg': 'black',
        'images_dir': 'images'
    },
    '黑夜主题': {
        'bg_color': 'black',
        'fg_color': 'white',
        'font': ("Microsoft YaHei", 18),
        'button_bg': 'black',
        'button_fg': 'white',
        'images_dir': 'images2'
    },
}

current_theme = "默认主题"

# 切换主题的函数
def switch_theme(theme_name):
    global current_theme
    global titleLabel, gamelistLabel, tip_label, zhuti
    current_theme = theme_name
    theme = themes[theme_name]
    root.config(bg=theme['bg_color'])
    titleLabel.place_forget()
    gamelistLabel.place_forget()
    tip_label.place_forget()
    zhuti.place_forget()

    if current_theme == "黑夜主题":
        titleLabel = tk.Label(root, text="BGGame Box", font=("Microsoft YaHei", 28, "bold"), bg="black", fg="white")
        gamelistLabel = tk.Label(root, text="游戏列表", font=("Microsoft YaHei", 28, "bold"), bg="black", fg="white")
        tip_label = tk.Label(root, text="", font=("Microsoft YaHei", 18), bg="black", fg="white")
        zhuti = tk.Label(root, text="主题", font=("Microsoft YaHei", 28, "bold"), bg="black", fg="white")
    else:
        titleLabel = tk.Label(root, text="BGGame Box", font=("Microsoft YaHei", 28, "bold"), bg="white", fg="black")
        gamelistLabel = tk.Label(root, text="游戏列表", font=("Microsoft YaHei", 28, "bold"), bg="white", fg="black")
        tip_label = tk.Label(root, text="", font=("Microsoft YaHei", 18), bg="white", fg="black")
        zhuti = tk.Label(root, text="主题", font=("Microsoft YaHei", 28, "bold"), bg="white", fg="black")
    titleLabel.place(x=180, y=10)
    tip_label.place(x=480, y=90)
    # 更新按钮图片
    update_button_images(theme['images_dir'])

# 更新按钮图片的函数
def update_button_images(images_dir):
    global Menubutton_game, Menubutton_user, Menubutton_sett
    # 更新游戏按钮图片
    icongame = Image.open(os.path.join(images_dir, 'game.png'))
    photo = ImageTk.PhotoImage(icongame)
    Menubutton_game.config(image=photo)
    Menubutton_game.image = photo
    # 更新用户按钮图片
    iconuser = Image.open(os.path.join(images_dir, 'user.png'))
    photo1 = ImageTk.PhotoImage(iconuser)
    Menubutton_user.config(image=photo1)
    Menubutton_user.image = photo1
    # 更新设置按钮图片
    iconsett = Image.open(os.path.join(images_dir, 'set.png'))
    photo2 = ImageTk.PhotoImage(iconsett)
    Menubutton_sett.config(image=photo2)
    Menubutton_sett.image = photo2

def update_tip_text():
    global tip_index
    tip_text = tips[tip_index]
    tip_index = random.randint(0, len(tips) - 1)
    tip_label.config(text=tip_text)
    current_font_size = tip_label.cget("font").split()[1]
    new_font_size = "20" if current_font_size == "18" else "18"
    tip_label.config(font=("Microsoft YaHei", new_font_size))
    root.after(1000, update_tip_text)

def get_Games():
    if not ".games" in os.listdir(gamepath):
        with open(gamepath + "/.games", "w", encoding="utf-8") as f:
            f.write("")
        update_Games()
    with open(gamepath + "/.games", "r", encoding="utf-8") as f:
        games = f.read().split("\n")
    if not games:
        update_Games()
    return games

def update_Games():
    global games
    if not ".games" in os.listdir(gamepath):
        with open(gamepath + "/.games", "w", encoding="utf-8") as f:
            f.write("")
        update_Games()
    games = os.listdir(gamepath)
    for i in range(len(games)):
        games[i] = games[i].split(".")[0].capitalize()
    del games[0]
    with open(gamepath + "/.games", "w", encoding="utf-8") as f:
        f.truncate(0)
        f.write("\n".join(games))
    games = get_Games()
    gameList.delete(0, last=tk.END)
    for item in games:
        gameList.insert(tk.END, item)

def run_Game(game):
    try:
        subprocess.Popen(["python", gamepath + os.path.sep + game.lower() + ".py"])
    except Exception as e:
        messagebox.showerror("Error", f"还没有选中任何游戏！{e}")

def delete_Game():
    try:
        global games
        result = messagebox.askokcancel(title='BGGame Launcher',
                                       message=f'确定删除游戏“{games[gameList.curselection()[0]]}”？')
        if result:
            game = games[gameList.curselection()[0]]
            gameList.delete(gameList.curselection()[0])
            os.remove(gamepath + os.path.sep + game.lower() + ".py")
            games.remove(game)
            update_Games()
    except IndexError:
        messagebox.showerror("Error", "还没有选中任何游戏！ ")
    except Exception as e:
        messagebox.showerror("Error", f"无法删除游戏：{str(e)}")

def add_Game():
    try:
        global games
        file_path = filedialog.askopenfilename(title="打开游戏", filetypes=[("Python 文件", ".py")])
        newgame = file_path.split('/')[-1].split('.')[0].capitalize()
        if file_path and not newgame in games:
            shutil.copy(file_path, gamepath)
            gameList.insert(tk.END, file_path.split('/')[-1].split('.')[0].capitalize())
        update_Games()
    except Exception as e:
        messagebox.showerror("Error", f"无法添加游戏：{str(e)}")

def turn_page(mode):
    global topage
    if mode == 0 and topage + 13 <= gameList.size():
        topage += 13
        gameList.yview_moveto(topage)
    elif mode == 13 and topage - 13 >= 0:
        topage -= 13
        gameList.yview_moveto(topage)

def go():
    try:
        selected = gameList.curselection()
        if not selected:
            raise ValueError("还没有选中任何游戏！")
        game = games[selected[0]]
        run_Game(game)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def change_menu():
    global menu
    if menu == 0:
        titleLabel.place(x=180, y=10)
        gameList.place(x=180, y=70)
        lastPageButton.place(x=180, y=500)
        nextPageButton.place(x=328, y=500)
        runButton.place(x=490, y=454)
        deleteButton.place(x=490, y=390)
        addButton.place(x=490, y=327)
        tip_label.place(x=480, y=90)
        zhuti.place_forget()
        themeComboBox.place_forget()
        gamelistLabel.place_forget()
        updateGamesListButton.place_forget()
        usernameLabel.place_forget()
    if menu == 1:
        titleLabel.place_forget()
        gameList.place_forget()
        lastPageButton.place_forget()
        nextPageButton.place_forget()
        runButton.place_forget()
        deleteButton.place_forget()
        addButton.place_forget()
        tip_label.place_forget()
        usernameLabel.place_forget()
        zhuti.place(x=180, y=10)
        themeComboBox.place(x=180, y=80)
        gamelistLabel.place(x=180, y=120)
        updateGamesListButton.place(x=180, y=190)
    if menu == 2:
        titleLabel.place_forget()
        gameList.place_forget()
        lastPageButton.place_forget()
        nextPageButton.place_forget()
        runButton.place_forget()
        deleteButton.place_forget()
        addButton.place_forget()
        tip_label.place_forget()
        zhuti.place_forget()
        themeComboBox.place_forget()
        gamelistLabel.place_forget()
        updateGamesListButton.place_forget()
        usernameLabel.place(x=180, y=10)
    root.after(100, change_menu)

def menuu(a):
    global menu
    if a == 0:
        menu = 0
        change_menu()
    elif a == 1:
        menu = 1
        change_menu()
    elif a == 2:
        menu = 2
        change_menu()

def ttheme(a):
    global theme
    theme = a

def themea():
    Menubutton_game.place_forget()
    Menubutton_user.place_forget()
    Menubutton_sett.place_forget()
    icongame = Image.open(r"images2/game.png")
    photo = ImageTk.PhotoImage(icongame)
    iconuser = Image.open(r"images2/user.png")
    photo1 = ImageTk.PhotoImage(iconuser)
    iconsett = Image.open(r"images2/set.png")
    photo2 = ImageTk.PhotoImage(iconsett)

try:
    if sys.argv[1] != "logen":
        sys.exit(0)
except IndexError:
    sys.exit(0)

root = tk.Tk()
root.title('BGGame Launcher')
root.geometry("770x550")
root.config(bg="white")
root.option_add("*TCombobox*Listbox.font", ("Microsoft YaHei", 15))

style = ttk.Style()
style.configure("TButton", font=("Microsoft YaHei", 15))

games = get_Games()
topage = 0

menu = 0
theme = 0

titleLabel = tk.Label(root, text="BGGame Box", font=("Microsoft YaHei", 28, "bold"), bg="white")
titleLabel.place(x=180, y=10)

gameList = tk.Listbox(root, height=13, font=("Microsoft YaHei", 18), bg="white", width=20)
gameList.place(x=180, y=70)

lastPageButton = tk.Button(root, text="上一页", command=lambda: turn_page(1), width=18, bg="white")
lastPageButton.place(x=180, y=500)

nextPageButton = tk.Button(root, text="下一页", command=lambda: turn_page(0), width=18, bg="white")
nextPageButton.place(x=328, y=500)

runButton = tk.Button(root, text="启动！", font=("Microsoft YaHei", 15),
                      command=go, width=21, height=2, activebackground="#D7E6F0", bg="white")
runButton.place(x=490, y=454)

deleteButton = tk.Button(root, text="删除游戏", font=("Microsoft YaHei", 15),
                      command=delete_Game, width=21, height=1, activebackground="#D7E6F0", bg="white")
deleteButton.place(x=490, y=390)

frame = tk.Frame(root, width = 160, height = 9999, highlightbackground="white", highlightcolor="white", highlightthickness=11)
frame.pack(side = tk.LEFT, fill = tk.Y)

addButton = tk.Button(root, text="添加游戏", font=("Microsoft YaHei", 15),
                      command=add_Game, width=21, height=1, activebackground="#D7E6F0", bg="white")
addButton.pack()
addButton.place(x=490, y=327)

zhuti = tk.Label(root, text="主题", font=("Microsoft YaHei", 28, "bold"), bg="white")
zhuti.place_forget()

var = tk.StringVar()
themeComboBox = ttk.Combobox(root, textvariable=var, value=("默认主题", "多彩主题", "黑夜主题"))
themeComboBox.current(0)
themeComboBox.configure(font=("Microsoft YaHei", 15))
themeComboBox.bind("<<ComboboxSelected>>", lambda event: switch_theme(var.get()))
themeComboBox.place_forget()

gamelistLabel = tk.Label(root, text="游戏列表", font=("Microsoft YaHei", 28, "bold"), bg="white")
gamelistLabel.place_forget()

usernameLabel = tk.Label(root, text=sys.argv[2], font=("Microsoft YaHei", 28, "bold"), bg="white")
usernameLabel.place_forget()

updateGamesListButton = ttk.Button(root, text="更新游戏列表", command=update_Games)
updateGamesListButton.place_forget()

tip_label = tk.Label(root, text="", font=("Microsoft YaHei", 18), bg="white")
tip_label.pack()
tip_label.place(x=480, y=90)
update_tip_text()

icongame = Image.open(r"images2/game.png")
photo = ImageTk.PhotoImage(icongame)
Menubutton_game = ttk.Button(frame, image=photo, command=lambda: menuu(0))
Menubutton_game.image = photo
Menubutton_game.place(x=0, y=0)
iconuser = Image.open(r"images2/user.png")
photo1 = ImageTk.PhotoImage(iconuser)
Menubutton_user = ttk.Button(frame, image=photo1, command=lambda: menuu(2))
Menubutton_user.image = photo
Menubutton_user.place(x=0, y=120)
iconsett = Image.open(r"images2/set.png")
photo2 = ImageTk.PhotoImage(iconsett)
Menubutton_sett = ttk.Button(frame, image=photo2, command=lambda: menuu(1))
Menubutton_sett.image = photo
Menubutton_sett.place(x=0, y=60)

for item in games:
    gameList.insert(tk.END, item)

root.mainloop()