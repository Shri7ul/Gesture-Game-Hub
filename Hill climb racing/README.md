# Hill Climb Racing — Hand Gesture Control (BlueStacks)

Control **Hill Climb Racing** using **hand position** with OpenCV + MediaPipe.
Works best on **BlueStacks** (Android emulator) where the game is mapped to keyboard keys.

---

## Requirements
- Windows / macOS / Linux
- Python 3.9+
- Webcam
- BlueStacks installed
- Hill Climb Racing installed inside BlueStacks

---

## Install Dependencies
From this folder:
```bash
pip install opencv-python mediapipe pynput
````

---

## BlueStacks Key Mapping

Make sure these keys are mapped in BlueStacks:

* **Right Arrow (→)** = Gas / Accelerate
* **Left Arrow (←)** = Brake / Reverse

(BlueStacks → Game controls / Key mapping)

---

## Run

```bash
python hand_hcr_control.py
```

A webcam window will open.

---

## How to Play

1. Open **Hill Climb Racing** in BlueStacks
2. Click inside the game window once (to focus it)
3. Keep the Python script running
4. Use your hand in front of the webcam:

### Gesture → Action

* Move hand to **left side** → press **←** (Brake/Reverse)
* Move hand to **right side** → press **→** (Gas)
* Keep hand in the **center** → release keys (no press)

---

## Tips

* Ensure the game window is focused, otherwise key presses won’t work.
* Use good lighting for stable tracking.
* If the camera doesn’t open, try changing the camera index in code:

  * `cv2.VideoCapture(0)` → `cv2.VideoCapture(1)`

---

## Exit

Press **Q** on the webcam window to quit.
