import tkinter as tk
from tkinter import StringVar
import os

class UIManager:
    def __init__(self, media_player):
        self.root = tk.Tk()
        self.root.title("Media Player Info")
        self.root.geometry("400x200")

        self.track_var = StringVar()
        self.status_var = StringVar()
        self.volume_var = StringVar()

        self.track_var.set("Now Playing")
        self.status_var.set("Status: Playing")
        self.volume_var.set(f"Volume: {media_player.volume}%")

        tk.Label(self.root, text="Gesture Controlled Media Player", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self.root, textvariable=self.track_var, font=("Arial", 12)).pack()
        tk.Label(self.root, textvariable=self.status_var, font=("Arial", 12)).pack()
        tk.Label(self.root, textvariable=self.volume_var, font=("Arial", 12)).pack()

        self.media_player = media_player

    def update(self):
        self.volume_var.set(f"Volume: {self.media_player.volume}%")
        self.status_var.set("Paused" if self.media_player.paused else "Playing")
        self.track_var.set(f"Now Playing: {os.path.basename(self.media_player.tracks[self.media_player.current_track])}")
        self.root.update()

    def shutdown(self):
        self.root.destroy()