# Chrome Dino — Gesture Control (✌️ = Jump)

Play the Chrome Dino game using hand gestures.
This version is designed for smoother gameplay:
- **✌️ (V sign)** triggers **Jump**
- **✊ (Fist)** triggers **Duck**
- **Open Palm / Normal hand** does nothing (safe default)

---

## Requirements
- Python 3.9+
- Webcam
- Google Chrome (or any Chromium-based browser)

---

## Open the Game
In Chrome address bar:
````

chrome://dino

````
(or turn off internet and refresh a page)

Click on the game area once to focus it.

---

## Install Dependencies
From this folder:
```bash
pip install opencv-python mediapipe pynput
````

---

## Run

```bash
python chrome_dino_gesture.py
```

A webcam window will open.

---

## How to Play

1. Start the Dino game (press Space once manually if needed)
2. Keep the Dino tab/window focused
3. Use gestures:

### Gesture → Action

* **✌️ V sign** → Jump (Space)
* **✊ Fist** → Duck (Down Arrow)
* **✋ Normal / Palm / Other** → No action (ready state)

---

## Notes / Troubleshooting

* If Jump doesn’t trigger reliably, use better lighting and keep the hand visible.
* If ✌️ detection feels strict, relax the condition in code (ring finger ignore):

  * Replace:
    `return index_up and middle_up and (not ring_up) and (not pinky_up)`
  * With:
    `return index_up and middle_up and (not pinky_up)`

---

## Exit

Press **Q** on the webcam window to quit.
