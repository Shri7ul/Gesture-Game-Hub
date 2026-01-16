import time
import cv2
import mediapipe as mp
from pynput.keyboard import Controller, Key

keyboard = Controller()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.65,
    min_tracking_confidence=0.65
)

cap = cv2.VideoCapture(0)

# ---- Swipe settings (tune if needed) ----
WINDOW_SEC = 0.18         # swipe detection time window
MIN_DIST = 0.12           # normalized distance threshold (0..1)
COOLDOWN = 0.25           # seconds between swipes
# ----------------------------------------

history = []  # (t, x, y) wrist positions
last_swipe_time = 0.0

def send_swipe(direction: str):
    # quick tap key
    if direction == "UP":
        keyboard.press(Key.up); keyboard.release(Key.up)
    elif direction == "DOWN":
        keyboard.press(Key.down); keyboard.release(Key.down)
    elif direction == "LEFT":
        keyboard.press(Key.left); keyboard.release(Key.left)
    elif direction == "RIGHT":
        keyboard.press(Key.right); keyboard.release(Key.right)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = hands.process(rgb)

    now = time.time()
    status = "No hand"

    if res.multi_hand_landmarks:
        lm = res.multi_hand_landmarks[0].landmark
        wrist = lm[0]  # wrist landmark
        x, y = wrist.x, wrist.y

        # Add to history
        history.append((now, x, y))

        # keep only last WINDOW_SEC
        cutoff = now - WINDOW_SEC
        while history and history[0][0] < cutoff:
            history.pop(0)

        # Need at least 2 points to compute displacement
        if len(history) >= 2 and (now - last_swipe_time) >= COOLDOWN:
            t0, x0, y0 = history[0]
            t1, x1, y1 = history[-1]

            dx = x1 - x0
            dy = y1 - y0

            # Determine dominant movement
            if abs(dx) > abs(dy) and abs(dx) >= MIN_DIST:
                if dx > 0:
                    send_swipe("RIGHT")
                    status = "SWIPE RIGHT → TURN RIGHT"
                else:
                    send_swipe("LEFT")
                    status = "SWIPE LEFT → TURN LEFT"
                last_swipe_time = now
                history.clear()

            elif abs(dy) >= MIN_DIST:
                # In image coords: smaller y = up
                if dy < 0:
                    send_swipe("UP")
                    status = "SWIPE UP → JUMP"
                else:
                    send_swipe("DOWN")
                    status = "SWIPE DOWN → SLIDE"
                last_swipe_time = now
                history.clear()
        else:
            status = "Tracking..."

        # Visualize wrist point
        cv2.circle(frame, (int(x * w), int(y * h)), 8, (0, 255, 0), -1)
    else:
        # no hand => clear history to avoid accidental swipe
        history.clear()

    cv2.putText(frame, status, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
    cv2.putText(frame, f"MIN_DIST={MIN_DIST} WINDOW={WINDOW_SEC}s CD={COOLDOWN}s",
                (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 2)

    cv2.imshow("Temple Run Gesture Control (Swipe)", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
