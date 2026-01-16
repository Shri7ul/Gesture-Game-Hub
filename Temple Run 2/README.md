# Temple Run 2 — Gesture Control (Swipe Only)

Play **Temple Run 2** using hand gestures with **OpenCV + MediaPipe**.
This project detects a quick hand “swipe” motion and sends **keyboard arrow keys**.

✅ Works great for browser version (e.g., Poki) and can work on emulators if arrow keys are mapped.

---

## Requirements
- Python 3.9+
- Webcam
- Windows / macOS / Linux
- A version of Temple Run 2 that supports keyboard arrows:
  - Browser version (Poki etc.) ✅
  - Emulator (BlueStacks) ✅ if key mapping is set

---

## Install Dependencies
From this folder:

```bash
pip install opencv-python mediapipe pynput
````

---

## Run

```bash
python temple_run_gesture.py
```

A webcam window will open.

---

## How It Works

The script tracks your **wrist position** (MediaPipe landmark 0) over a short time window.
If your hand moves fast enough in a direction, it triggers a swipe action:

### Gesture → Action (Keyboard)

* Swipe hand **UP**    → **Up Arrow (↑)**  = Jump
* Swipe hand **DOWN**  → **Down Arrow (↓)** = Slide
* Swipe hand **LEFT**  → **Left Arrow (←)** = Move Left / Turn Left
* Swipe hand **RIGHT** → **Right Arrow (→)** = Move Right / Turn Right

---

## How to Play (Best Practice)

1. Open Temple Run 2 (browser/emulator)
2. Click inside the game window once (focus is required)
3. Run the Python script
4. Do quick hand swipes in front of the webcam

Tip: Fast, clear swipes work better than slow moves.

---

## Tuning (Optional)

Inside the code you can adjust:

* `MIN_DIST`

  * Lower = easier to trigger (more sensitive)
  * Higher = harder to trigger (less false triggers)
    Example: `0.10` to `0.15`

* `COOLDOWN`

  * Lower = faster repeated swipes
  * Higher = prevents accidental double triggers
    Example: `0.18` to `0.35`

* `WINDOW_SEC`

  * Shorter window = sharper swipe detection
  * Longer window = smoother but may feel delayed
    Example: `0.14` to `0.22`

---

## Troubleshooting

### Game doesn’t respond to gestures

* Make sure the game window is focused (click inside the game)
* Test arrow keys manually in the game
* If using an emulator, confirm key mappings for arrows

### Camera doesn’t open

Try changing camera index in code:

* `cv2.VideoCapture(0)` → `cv2.VideoCapture(1)`

---

## Exit

Press **Q** in the webcam window to quit.