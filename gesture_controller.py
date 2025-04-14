import mediapipe as mp
import time
import cv2

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
last_swipe_time = time.time()
swipe_threshold = 0.2
pinch_active = False
initial_y = None


def detect_gesture(frame, media_player):
    global last_swipe_time, pinch_active, initial_y

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

            # Closed fist = pause
            if is_closed_fist(hand_landmarks.landmark):
                media_player.pause()

            # Open hand = resume
            elif is_open_hand(hand_landmarks.landmark):
                media_player.resume()

            # Pinch = volume
            pinch_distance = ((thumb_tip.x - index_tip.x)**2 + (thumb_tip.y - index_tip.y)**2) ** 0.5
            if pinch_distance < 0.05:
                if not pinch_active:
                    pinch_active = True
                    initial_y = index_tip.y
                else:
                    delta_y = initial_y - index_tip.y
                    if abs(delta_y) > 0.01:
                        media_player.adjust_volume(delta_y)
                        initial_y = index_tip.y
            else:
                pinch_active = False

            # Swipe = change track
            current_time = time.time()
            if current_time - last_swipe_time > 1:
                swipe_distance = abs(wrist.x - index_tip.x)
                if wrist.x - index_tip.x > swipe_threshold and swipe_distance > swipe_threshold:
                    media_player.next_track()
                    last_swipe_time = current_time
                elif index_tip.x - wrist.x > swipe_threshold and swipe_distance > swipe_threshold:
                    media_player.prev_track()
                    last_swipe_time = current_time

    return frame


def is_closed_fist(landmarks):
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    return all(finger.y > thumb_tip.y for i, finger in enumerate(landmarks) if i in [8, 12, 16, 20])


def is_open_hand(landmarks):
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    return all(finger.y < thumb_tip.y for i, finger in enumerate(landmarks) if i in [8, 12, 16, 20])