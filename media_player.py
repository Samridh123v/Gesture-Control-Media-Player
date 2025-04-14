import pygame
import os

class MediaPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.media_folder = "media_files"
        self.tracks = [os.path.join(self.media_folder, f) for f in os.listdir(self.media_folder) if f.endswith(".mp3")]
        self.current_track = 0
        self.volume = 50
        self.paused = False
        if not self.tracks:
            raise FileNotFoundError("No .mp3 files found in 'media_files'")
        pygame.mixer.music.load(self.tracks[self.current_track])
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(self.volume / 100)

    def pause(self):
        if not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
            print("[MediaPlayer] Paused")

    def resume(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
            print("[MediaPlayer] Resumed")

    def adjust_volume(self, delta_y):
        self.volume += int(delta_y * 100)
        self.volume = max(0, min(100, self.volume))
        pygame.mixer.music.set_volume(self.volume / 100)
        print(f"[MediaPlayer] Volume: {self.volume}%")

    def next_track(self):
        self.current_track = (self.current_track + 1) % len(self.tracks)
        self.load_track()

    def prev_track(self):
        self.current_track = (self.current_track - 1) % len(self.tracks)
        self.load_track()

    def load_track(self):
        pygame.mixer.music.load(self.tracks[self.current_track])
        pygame.mixer.music.play(-1)
        print(f"[MediaPlayer] Now Playing: {os.path.basename(self.tracks[self.current_track])}")