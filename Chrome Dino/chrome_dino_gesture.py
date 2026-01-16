import time
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

cap = cv2.VideoCapture(0)

# Tunables
JUMP_COOLDOWN = 0.22   # small cooldown to prevent double-trigger
last_jump_time = 0.0
jump_ready = True      # requires release (neutral) to re-arm

ducking = False

def finger_extended(lm, tip, pip):
    # In MediaPipe image coordinates: smaller y = higher (finger up)
    return lm[tip].y < lm[pip].y

def is_fist(lm):
    # all four fingers folded
    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]
    return all(lm[t].y > lm[p].y for t, p in zip(tips, pips))

def is_v_sign(lm):
    # Index + Middle up, Ring + Pinky down
    index_up  = finger_extended(lm, 8, 6)
    middle_up = finger_extended(lm, 12, 10)
    ring_up   = finger_extended(lm, 16, 14)
    pinky_up  = finger_extended(lm, 20, 18)

    # thumb ignored (varies a lot)
    return index_up and middle_up and (not ring_up) and (not pinky_up)

def do_jump():
    keyboard.press(Key.space)
    keyboard.release(Key.space)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    now = time.time()
    status = "No Hand"

    gesture = "NONE"
    if result.multi_hand_landmarks:
        lm = result.multi_hand_landmarks[0].landmark

        if is_fist(lm):
            gesture = "FIST"
        elif is_v_sign(lm):
            gesture = "V"
        else:
            gesture = "PALM_OR_OTHER"

    # ---- Duck (hold) ----
    if gesture == "FIST":
        if not ducking:
            keyboard.press(Key.down)
            ducking = True
        # while ducking, don't jump
        jump_ready = False
        status = "✊ FIST → DUCK (hold)"

    else:
        if ducking:
            keyboard.release(Key.down)
            ducking = False

        # ---- Jump: ✌️ only, with tiny cooldown + re-arm on release ----
        if gesture == "V":
            if jump_ready and (now - last_jump_time) >= JUMP_COOLDOWN:
                do_jump()
                last_jump_time = now
                jump_ready = False  # must release to normal first
                status = "✌️ V → JUMP"
            else:
                status = "✌️ V (waiting)"
        else:
            # normal palm/other/no-hand = re-arm
            jump_ready = True
            status = "✋ NORMAL (ready)"

    cv2.putText(frame, status, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.95, (0, 255, 0), 2)

    cv2.imshow("Chrome Dino Gesture Control (V=Jump)", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

keyboard.release(Key.down)
cap.release()
cv2.destroyAllWindows()
