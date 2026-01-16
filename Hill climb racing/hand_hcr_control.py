import cv2
import mediapipe as mp
from pynput.keyboard import Controller, Key

keyboard = Controller()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)
mp_draw = mp.solutions.drawing_utils

# state to avoid spamming
pressed_left = False
pressed_right = False

def press_left():
    global pressed_left
    if not pressed_left:
        keyboard.press(Key.left)
        pressed_left = True

def release_left():
    global pressed_left
    if pressed_left:
        keyboard.release(Key.left)
        pressed_left = False

def press_right():
    global pressed_right
    if not pressed_right:
        keyboard.press(Key.right)
        pressed_right = True

def release_right():
    global pressed_right
    if pressed_right:
        keyboard.release(Key.right)
        pressed_right = False

cap = cv2.VideoCapture(0)

# screen split threshold (center)
# You can tune this based on your camera view
CENTER = 0.5
DEADZONE = 0.08  # ignore small movement near center

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        handLms = result.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

        # use wrist (landmark 0) as hand position
        wrist = handLms.landmark[0]
        x = wrist.x  # normalized 0..1

        # visualize center line
        cx = int(CENTER * w)
        cv2.line(frame, (cx, 0), (cx, h), (0, 255, 0), 2)

        # decision
        if x < CENTER - DEADZONE:
            press_left()
            release_right()
            status = "LEFT"
        elif x > CENTER + DEADZONE:
            press_right()
            release_left()
            status = "RIGHT"
        else:
            release_left()
            release_right()
            status = "CENTER"

        cv2.putText(frame, f"Hand: {status}  x={x:.2f}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    else:
        # no hand = release keys
        release_left()
        release_right()
        cv2.putText(frame, "No hand", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("HCR Hand Control", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# cleanup
release_left()
release_right()
cap.release()
cv2.destroyAllWindows()
