import sys
import os
import pygame
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import webbrowser
import subprocess
import time
import urllib.request

# === BASE ===
BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
CLICK_SOUND_PATH = os.path.join(BASE_DIR, "assets", "click.wav")
BG_IMAGE_PATH = os.path.join(BASE_DIR, "assets", "background.png")
LOGO_IMAGE_PATH = os.path.join(BASE_DIR, "assets", "logo.png")
CROSSHAIR_EXE = os.path.join(BASE_DIR, "assets", "crosshair.exe")
CHATGPT_EXE = os.path.join(BASE_DIR, "assets", "chatgpt.exe")
WALLPAPER_EXE = os.path.join(BASE_DIR, "assets", "livelywallpaper.exe")
WARP_TUTORIAL_PATH = os.path.join(BASE_DIR, "assets", "tutorialwarp.txt")

# === CHECK FOR UPDATES ===
def check_for_updates():
    import zipfile, io, shutil
    try:
        update_url = "https://raw.githubusercontent.com/your-username/your-repo/main/version.txt"
        zip_url = "https://github.com/your-username/your-repo/archive/refs/heads/main.zip"
        
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
                with urllib.request.urlopen(zip_url) as zip_resp:
                    with zipfile.ZipFile(io.BytesIO(zip_resp.read())) as zf:
                        temp_dir = os.path.join(BASE_DIR, "update_temp")
                        if os.path.exists(temp_dir): shutil.rmtree(temp_dir)
                        zf.extractall(temp_dir)
                        extracted_path = os.path.join(temp_dir, os.listdir(temp_dir)[0])

                        # Copy semua file ke direktori utama
                        for root_dir, _, files in os.walk(extracted_path):
                            for file in files:
                                src_path = os.path.join(root_dir, file)
                                rel_path = os.path.relpath(src_path, extracted_path)
                                dst_path = os.path.join(BASE_DIR, rel_path)
                                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                                shutil.copy2(src_path, dst_path)
                        messagebox.showinfo("Update", "Launcher berhasil diperbarui. Silakan restart.")
                        sys.exit()
    except Exception as e:
        print(f"Gagal memeriksa update: {e}")

check_for_updates():
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
        print(f"Gagal memeriksa update: {e}")

check_for_updates()

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

show_loading_screen()

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

# === FUNGSI ===
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

# Tambahkan UI & tombol lainnya di sini sesuai kebutuhan

root.mainloop()
