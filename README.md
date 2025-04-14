This is a media player that can play .mp3 files. You can control the Tracks and Volume using only your hand gestures!

🎮 Gesture Controls Overview
✊ Closed Fist
Action: Pauses the music.

Logic: All fingertips (except thumb) are below the thumb → considered a fist.

🖐️ Open Hand
Action: Resumes the music if it's paused.

Logic: All fingertips (except thumb) are above the thumb → considered an open hand.

🤏 Pinch Gesture (Thumb + Index Finger Close Together)
Action: Adjusts volume up/down.

How it works:

When pinch starts, it captures initial y-position of the index finger.

If you move the pinch upwards, volume increases.

If you move the pinch downwards, volume decreases.

Sensitivity: Based on how much the y position changes.

👉➡️ Swipe Right (Wrist to Index moves right)
Action: Skips to the next track.

Condition: Enough horizontal distance (swipe_threshold) between wrist and index tip in the rightward direction.

👈⬅️ Swipe Left (Wrist to Index moves left)
Action: Goes to the previous track.

Condition: Same distance check, but in the leftward direction.

💡 Bonus Notes:
Music loops indefinitely unless skipped or paused.

A GUI shows the track name, play/pause status, and volume using Tkinter.

Track switching has a cooldown of 1 second to prevent accidental double-swipes.
