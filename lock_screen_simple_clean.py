"""
===================================================================
Rickroll Lock Screen - BadUSB Demo Project
=====================================================
Author:      Irem Dönmez
Date:        2026-02-19
Version:     1.2
Description: Displays a fullscreen rickroll image with music for 33 seconds.
             Created as educational cybersecurity demonstration tool.
             Made with the help of AI
============================================================================
"""

import sys
import os
import tkinter as tk
from PIL import Image, ImageTk
import time
import threading

LOCK_TIME_SECONDS = 33
IMAGE_FILENAME = "get_rickrolled.jpg"
MUSIC_FILENAME = "song.mp3"

def getResourcePath(filename):
    """Get file path (works in .exe and normal script)"""
    basePath = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(basePath, filename)


def playMusic(musicPath):
    """Play MP3 in background without extra window"""
    if os.path.exists(musicPath):
        try:
            from playsound import playsound
            playsound(musicPath, block=False)
        except Exception as e:
            print(f"Music error: {e}")

def closeAfterDelay(window, seconds):
    """Close window after delay"""
    time.sleep(seconds)
    window.destroy()


def main():
    """Main program, shows rickroll for 33 seconds"""
    
    # Get file paths
    imagePath = getResourcePath(IMAGE_FILENAME)
    musicPath = getResourcePath(MUSIC_FILENAME)
    
    # Create fullscreen window
    window = tk.Tk()
    window.attributes("-fullscreen", True)
    window.attributes("-topmost", True)
    window.configure(bg="black")
    
    # Load and resize image
    image = Image.open(imagePath)
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    image = image.resize((screenWidth, screenHeight), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    
    # Display image
    label = tk.Label(window, image=photo, bg="black")
    label.image = photo  # Keep reference
    label.pack(fill="both", expand=True)
    
    # Start music thread
    threading.Thread(target=playMusic, args=(musicPath,), daemon=True).start()
    
    # Start close timer thread
    threading.Thread(target=closeAfterDelay, args=(window, LOCK_TIME_SECONDS), daemon=True).start()
    
    # Run programm
    window.mainloop()


if __name__ == "__main__":
    main()
