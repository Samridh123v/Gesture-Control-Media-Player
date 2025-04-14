# Gesture-Controlled Media Player

This is a media player that can play .mp3 files and allows you to control the tracks and volume using **only hand gestures**!

## 🎮 Gesture Controls Overview

### ✊ **Closed Fist Action**  
**Action:** Pauses the music.  
**Logic:** All fingertips (except the thumb) are below the thumb → considered a fist.

### 🖐️ Open Hand Action 
**Action:** Resumes the music if it's paused.  
**Logic:** All fingertips (except the thumb) are above the thumb → considered an open hand.

### 🤏 **Pinch Gesture (Thumb + Index Finger Close Together)**  
**Action:** Adjusts volume up or down.  
**How it works:**  
- When the pinch starts, it captures the initial y-position of the index finger.  
- Moving the pinch upwards increases the volume.  
- Moving the pinch downwards decreases the volume.  
**Sensitivity:** Based on the change in the y-position of the index finger.

### 👉➡️ **Swipe Right** (Wrist to Index moves right)  
**Action:** Skips to the next track.  
**Condition:** Horizontal swipe with enough distance between wrist and index tip in the rightward direction.

### 👈⬅️ **Swipe Left** (Wrist to Index moves left)  
**Action:** Goes to the previous track.  
**Condition:** Horizontal swipe with enough distance between wrist and index tip in the leftward direction.

## 💡 Additional Notes
- Music loops indefinitely unless skipped or paused.
- A GUI shows the track name, play/pause status, and volume using **Tkinter**.
- Track switching has a cooldown of **1 second** to prevent accidental double-swipes.


## 🚀 How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/gesture-media-player.git
   cd gesture-media-player

