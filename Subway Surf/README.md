# Subway Surfers — Gesture Control (Hybrid: Lane Hold + Swipe Jump/Roll)

Control **Subway Surfers** (BlueStacks) using **hand gestures** with OpenCV + MediaPipe.

This project uses a **hybrid control** approach:
- **Lane change (Left/Right)** is based on **hand X position** (hold in left/right zone)
- **Jump / Roll** is based on **quick hand swipe (Up/Down)**

This makes coin/point collection much easier than pure swipe-only control.

---

## Requirements
- Python 3.9+
- Webcam
- BlueStacks installed
- Subway Surfers installed inside BlueStacks

---

## Install Dependencies
From this folder:

```bash
pip install opencv-python mediapipe pynput
````

---

## BlueStacks Key Mapping (Important)

Ensure Subway Surfers is mapped to keyboard keys:

* **Left Arrow (←)**  = Move to left lane
* **Right Arrow (→)** = Move to right lane
* **Up Arrow (↑)**    = Jump
* **Down Arrow (↓)**  = Roll / Slide

Open in BlueStacks:

* Game controls / Key mapping
* Add or edit mappings if needed

---

## Run

```bash
python subway_surfers_gesture.py
```

A webcam window will open.

---

## How to Play

1. Open **Subway Surfers** in BlueStacks
2. Click inside the game window once (to focus it)
3. Keep the Python script running
4. Use gestures in front of the webcam:

### Gestures → Actions

**Lane Control (Hold-based)**

* Move hand to the **left zone** → lane left (←)
* Move hand to the **right zone** → lane right (→)
* Keep hand in the **center** → no lane change

**Jump / Roll (Swipe-based)**

* Quick hand **up swipe** → Jump (↑)
* Quick hand **down swipe** → Roll/Slide (↓)

---

## Tips for Better Tracking

* Use good lighting (avoid backlight)
* Keep your hand fully visible
* Keep game window focused, otherwise inputs won't work
* For smoother lane control, move hand clearly into left/right zones

---

## Tuning (Optional)

If lane changes are too sensitive or too slow, edit these values in code:

* `LANE_LEFT_TH`, `LANE_RIGHT_TH` (zone width)
* `LANE_COOLDOWN` (time between lane switches)

If jump/roll misses:

* Lower `SWIPE_MIN_DY` slightly (e.g., 0.10)
* Increase `SWIPE_WINDOW` slightly (e.g., 0.18)

---

## Exit

Press **Q** on the webcam window to quit.
