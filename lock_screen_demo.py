import sys
import os
import tkinter as tk
from PIL import Image, ImageTk
import time
import threading

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base_path, relative_path)

IMAGE_PATH = resource_path("get_rickrolled.jpg")
MP3_PATH = resource_path("song.mp3")
LOCK_TIME = 20

def play_music():
    if os.path.exists(MP3_PATH):
        try:
            os.startfile(MP3_PATH)
        except Exception as e:
            print("Musikfehler", e)
    else:
        print("MP3 fehlt")

def close_after_delay(root):
    time.sleep(LOCK_TIME)
    root.after(0, root.destroy)

root = tk.Tk()
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.configure(bg="black")

if not os.path.exists(IMAGE_PATH):
    raise RuntimeError("Bilddatei fehlt")

img = Image.open(IMAGE_PATH)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
img = img.resize((screen_width, screen_height), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)

label = tk.Label(root, image=photo, bg="black")
label.image = photo
label.pack(fill="both", expand=True)

threading.Thread(target=play_music, daemon=True).start()
threading.Thread(target=close_after_delay, args=(root,), daemon=True).start()

root.mainloop()
