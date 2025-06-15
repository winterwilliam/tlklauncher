import sys
import os
import pygame
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import webbrowser
import subprocess
import time
import urllib.request

# === LOADING SCREEN ===
def show_loading_screen():
    splash = tk.Tk()
    splash.overrideredirect(True)
    splash.geometry("400x200+{}+{}".format(
        splash.winfo_screenwidth() // 2 - 200,
        splash.winfo_screenheight() // 2 - 100
    ))
    splash.configure(bg="black")

    tk.Label(splash, text="Loading...", font=("Arial", 20), fg="white", bg="black").pack(pady=30)
    tk.Label(splash, text="Created by WinterWilliam", font=("Arial", 10), fg="gray", bg="black").pack()

    progress = ttk.Progressbar(splash, orient="horizontal", length=300, mode="indeterminate")
    progress.pack(pady=20)
    progress.start(10)

    try:
        pygame.mixer.init()
        preload_music = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets", "preload_music.wav"))
        preload_music.set_volume(0.2)
        preload_music.play()
    except:
        pass

    splash.update()
    splash.after(3000, splash.destroy)
    splash.mainloop()

# === BASE ===
BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

CLICK_SOUND_PATH = os.path.join(BASE_DIR, "assets", "click.wav")
BG_IMAGE_PATH = os.path.join(BASE_DIR, "assets", "background.png")
LOGO_IMAGE_PATH = os.path.join(BASE_DIR, "assets", "logo.png")
CROSSHAIR_EXE = os.path.join(BASE_DIR, "assets", "crosshair.exe")
CHATGPT_EXE = os.path.join(BASE_DIR, "assets", "chatgpt.exe")
WALLPAPER_EXE = os.path.join(BASE_DIR, "assets", "livelywallpaper.exe")
WARP_TUTORIAL_PATH = os.path.join(BASE_DIR, "assets", "tutorialwarp.txt")

show_loading_screen()

# === CHECK FOR UPDATES ===
def check_for_updates():
    try:
        update_url = "https://raw.githubusercontent.com/winterwilliam/tlklauncher/main/version.txt"
        with urllib.request.urlopen(update_url) as response:
            latest_version = response.read().decode("utf-8").strip()
        current_version_path = os.path.join(BASE_DIR, "version.txt")
        if os.path.exists(current_version_path):
            with open(current_version_path, "r") as f:
                current_version = f.read().strip()
        else:
            current_version = "0.0.0"

        if latest_version != current_version:
            if messagebox.askyesno("Update Available", f"Versi baru {latest_version} tersedia. Ingin update?"):
                webbrowser.open("https://github.com/winterwilliam/tlklauncher/releases/latest")
    except Exception as e:
        print("Gagal memeriksa update:", e)

check_for_updates()

# === SOUND ===
pygame.mixer.init()
click_sound = pygame.mixer.Sound(CLICK_SOUND_PATH)

def play_click():
    click_sound.play()

# === SAFE IMAGE LOAD ===
def safe_load_image(path):
    try:
        return tk.PhotoImage(file=path)
    except Exception as e:
        messagebox.showerror("Gagal Memuat", f"Gagal memuat file: {path}\n\n{e}")
        return None

# === APP ===
root = tk.Tk()
root.title("TLK Game Launcher")
root.geometry("800x500")

crosshair_proc = None

# === FUNCTIONS ===
def open_redm(): play_click(); webbrowser.open("fivem://connect/cfx.re/join/374xjb")
def open_fivem(): play_click(); webbrowser.open("redm://connect/cfx.re/join/ov3vy7")
def open_website(): play_click(); webbrowser.open("https://thelastknightst.id")
def open_discord(): play_click(); webbrowser.open("https://discord.gg/Ww45HgqPpk")
def open_tiktok(): play_click(); webbrowser.open("https://www.tiktok.com/@winterdegarcia/")
def open_instagram(): play_click(); webbrowser.open("https://www.instagram.com/winterwilliam_/")
def open_gmail(): play_click(); webbrowser.open("https://mail.google.com")
def open_calendar(): play_click(); subprocess.Popen(["start", "outlookcal:"], shell=True)
def open_calc(): play_click(); subprocess.Popen("calc")
def open_notepad(): play_click(); subprocess.Popen("notepad")

def toggle_crosshair():
    global crosshair_proc
    play_click()
    if not os.path.exists(CROSSHAIR_EXE):
        messagebox.showerror("Gagal", "crosshair.exe tidak ditemukan.")
        return
    if crosshair_proc is None:
        crosshair_proc = subprocess.Popen([CROSSHAIR_EXE], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        crosshair_proc.terminate(); crosshair_proc = None

def open_settings():
    play_click()
    def apply_theme():
        selected = theme_var.get()
        root.config(bg="#111" if selected == "Dark" else "#f0f0f0")

    def change_background():
        filepath = filedialog.askopenfilename(filetypes=[["PNG Images", "*.png"]])
        if filepath:
            new_bg = tk.PhotoImage(file=filepath)
            bg_label.configure(image=new_bg)
            bg_label.image = new_bg

    settings_window = tk.Toplevel(root)
    settings_window.title("Pengaturan Tema")
    settings_window.geometry("300x200")

    theme_var = tk.StringVar(value="Dark")
    tk.Label(settings_window, text="Pilih Tema:").pack(pady=10)
    tk.Radiobutton(settings_window, text="Dark", variable=theme_var, value="Dark").pack()
    tk.Radiobutton(settings_window, text="Light", variable=theme_var, value="Light").pack()
    tk.Button(settings_window, text="Terapkan Tema", command=apply_theme).pack(pady=10)
    tk.Button(settings_window, text="Ganti Background", command=change_background).pack(pady=5)

def open_wallpaper(): play_click(); subprocess.Popen([WALLPAPER_EXE]) if os.path.exists(WALLPAPER_EXE) else messagebox.showerror("Gagal", "Wallpaper tidak ditemukan.")
def open_mods(): play_click(); webbrowser.open("https://drive.google.com/file/d/1P38jGarsMZo0FupIvzAd4L2WO86bYV13/view?usp=sharing")
def open_reshade(): play_click(); webbrowser.open("https://drive.google.com/file/d/1P38jGarsMZo0FupIvzAd4L2WO86bYV13/view?usp=sharing")
def open_warp():
    play_click(); webbrowser.open("https://one.one.one.one/")
    os.startfile(WARP_TUTORIAL_PATH) if os.path.exists(WARP_TUTORIAL_PATH) else messagebox.showerror("Gagal", "tutorialwarp.txt tidak ditemukan.")
def open_chatgpt(): play_click(); subprocess.Popen([CHATGPT_EXE]) if os.path.exists(CHATGPT_EXE) else messagebox.showerror("Gagal", "chatgpt.exe tidak ditemukan.")

def open_other_menu():
    play_click()
    other = tk.Toplevel(root)
    other.title("OTHER")
    other.geometry("250x250")
    other.configure(bg="black")
    tk.Button(other, text="Calculator", font=("Arial", 12), width=20, command=open_calc).pack(pady=5)
    tk.Button(other, text="Notepad", font=("Arial", 12), width=20, command=open_notepad).pack(pady=5)
    tk.Button(other, text="Gmail", font=("Arial", 12), width=20, command=open_gmail).pack(pady=5)
    tk.Button(other, text="Calendar", font=("Arial", 12), width=20, command=open_calendar).pack(pady=5)

# === UI ===
bg_image = safe_load_image(BG_IMAGE_PATH)
if bg_image:
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

logo_image = safe_load_image(LOGO_IMAGE_PATH)
if logo_image:
    logo_label = tk.Label(root, image=logo_image, bg="#000")
    logo_label.pack(pady=10)

style = {"padx": 20, "pady": 10, "bg": "#222", "fg": "white", "font": ("Arial", 14), "width": 20}

# Tombol utama
tk.Button(root, text="Launch RedM", command=open_redm, **style).pack(pady=5)
tk.Button(root, text="Launch FiveM", command=open_fivem, **style).pack(pady=5)
tk.Button(root, text="Open Website", command=open_website, **style).pack(pady=5)
tk.Button(root, text="Toggle Crosshair", command=toggle_crosshair, **style).pack(pady=5)
tk.Button(root, text="Wallpaper", command=open_wallpaper, **style).pack(pady=5)

# Menu Other
tk.Button(root, text="OTHER", command=open_other_menu, bg="#666", fg="white", font=("Arial", 10, "bold")).place(relx=0.0, x=10, y=10)

# Jam Digital
clock_label = tk.Label(root, font=("Consolas", 12), bg="#000", fg="white")
clock_label.place(relx=0.0, rely=1.0, anchor='sw', x=10, y=-10)
def update_clock():
    now = time.strftime("%H:%M:%S")
    clock_label.config(text=now)
    root.after(1000, update_clock)
update_clock()

##tk.Button(root, text="⚙", font=("Arial", 9), command=lambda: subprocess.Popen("timedate.cpl")).place(relx=0.0, rely=1.0, anchor='sw', x=60, y=-12)

# === TOP-RIGHT BUTTONS ===
tk.Button(root, text="⚙", command=open_settings, bg="#444", fg="white", font=("Arial", 12, "bold")).place(relx=1.0, x=-10, y=10, anchor="ne")
tk.Button(root, text="MODS", command=open_mods, bg="#555", fg="white", font=("Arial", 9, "bold")).place(relx=1.0, x=-70, y=10, anchor="ne")
tk.Button(root, text="WARP", command=open_warp, bg="#444", fg="white", font=("Arial", 9, "bold")).place(relx=1.0, x=-130, y=10, anchor="ne")
tk.Button(root, text="RESHADE", command=open_reshade, bg="#333", fg="white", font=("Arial", 9, "bold")).place(relx=1.0, x=-200, y=10, anchor="ne")

# === BOTTOM-RIGHT SOCIAL BUTTONS ===
margin_right = 10
margin_bottom = 10
button_height = 30
gap = 5

tk.Button(root, text="JOIN DISCORD", command=open_discord, bg="#5865F2", fg="white", font=("Arial", 9, "bold"), width=15).place(relx=1.0, rely=1.0, anchor='se', x=-margin_right, y=-margin_bottom)
tk.Button(root, text="TIKTOK", command=open_tiktok, bg="#000000", fg="white", font=("Arial", 9, "bold"), width=15).place(relx=1.0, rely=1.0, anchor='se', x=-margin_right, y=-(margin_bottom + button_height + gap))
tk.Button(root, text="INSTAGRAM", command=open_instagram, bg="#C13584", fg="white", font=("Arial", 9, "bold"), width=15).place(relx=1.0, rely=1.0, anchor='se', x=-margin_right, y=-(margin_bottom + 2*(button_height + gap)))
tk.Button(root, text="SPOTIFY", command=lambda: subprocess.Popen(["spotify"]), bg="#1DB954", fg="white", font=("Arial", 9, "bold"), width=15).place(relx=1.0, rely=1.0, anchor='se', x=-margin_right, y=-(margin_bottom + 3*(button_height + gap)))
tk.Button(root, text="CHATGPT", command=open_chatgpt, bg="#333333", fg="white", font=("Arial", 9, "bold"), width=15).place(relx=1.0, rely=1.0, anchor='se', x=-margin_right, y=-(margin_bottom + 4*(button_height + gap)))

root.mainloop()