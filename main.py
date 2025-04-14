import cv2
from gesture_controller import detect_gesture
from media_player import MediaPlayer
from ui_manager import UIManager
import pygame
import sys

# Init
camera = cv2.VideoCapture(0)
media_player = MediaPlayer()
ui = UIManager(media_player)

print("\n[INFO] Gesture Media Player Running — press 'q' to quit\n")

try:
    while camera.isOpened():
        success, frame = camera.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        gesture = detect_gesture(frame, media_player)

        ui.update()
        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\n[INFO] Exiting...")

finally:
    camera.release()
    cv2.destroyAllWindows()
    pygame.quit()
    ui.shutdown()
    sys.exit()