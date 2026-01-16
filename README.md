# 🎮 Gesture Game Hub
**Play games using hand gestures with OpenCV & MediaPipe**

Gesture Game Hub is a collection of mini-projects where popular games are controlled using **real-time hand gestures** detected via a webcam.

This repository focuses on **practical computer vision**, **human–computer interaction**, and **gesture-based control systems**, built with Python.

---

## ✨ Key Features
- 🎥 Real-time hand tracking using **MediaPipe**
- 🖐️ Gesture-based controls (swipe, hold, pose)
- 🎮 Multiple games, each as a standalone mini-project
- ⌨️ Keyboard / emulator friendly (no game modding)
- 🧠 Clean logic designed for learning & experimentation

---

## 🧰 Tech Stack
- **Python**
- **OpenCV**
- **MediaPipe**
- **pynput** (keyboard control)
- Webcam input

---

## 📁 Project Structure
```

gesture-game-hub/
│
├── games/
│   ├── hill_climb_racing/
│   │   ├── hand_hcr_control.py
│   │   └── README.md
│   │
│   ├── chrome_dino/
│   │   ├── chrome_dino_gesture.py
│   │   └── README.md
│   │
│   ├── subway_surfers/
│   │   ├── subway_surfers_gesture.py
│   │   └── README.md
│   │
│   └── temple_run_2/
│       ├── temple_run_gesture.py
│       └── README.md
│
├── requirements.txt
└── README.md

````

Each game folder contains:
- A runnable Python script
- A dedicated README with usage instructions

---

## 🎯 Available Games

### 🏁 Hill Climb Racing (Emulator)
- Hand position controls gas & brake
- Works on BlueStacks
- Focus: Continuous control using hand X-position

### 🦖 Chrome Dino
- ✌️ Gesture = Jump
- ✊ Gesture = Duck
- Focus: Gesture classification & intentional triggers

### 🚆 Subway Surfers
- Swipe-based gesture control
- Optimized for coin collection
- Focus: Fast motion detection

### 🏃 Temple Run 2 (Browser / Emulator)
- Swipe gestures for jump, slide, turn
- Works smoothly on browser versions (e.g., Poki)
- Focus: Velocity-based gesture detection

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Shri7ul/Gesture-Game-Hub.git
cd gesture-game-hub
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run a game

Go to any game folder and run the script:

```bash
python <script_name>.py
```

Make sure:

* Webcam is connected
* Game window is focused

---

## 💡 Design Philosophy

* No game hacking or memory injection
* Uses **keyboard emulation** only
* Modular & extensible design
* Each mini-project teaches a specific CV/gesture concept

---

## 🧪 Who Is This For?

* Computer Vision learners
* AI / ML students
* Python developers
* Anyone interested in gesture-based interaction
* Portfolio & demo project builders

---

## 🔮 Future Plans

* 🎮 More games (Racing, Rhythm, FPS training)
* ⚙️ Unified launcher
* 📊 FPS & latency overlay
* 🧩 Config-driven gesture mappings
* 🖱️ Gesture → mouse control experiments

---

## 📜 Disclaimer

This project is for **educational and experimental purposes only**.
All games belong to their respective owners.

---

## 🤝 Contributions

Contributions, ideas, and improvements are welcome!

Feel free to fork the repo and experiment with new gesture ideas 🚀

---
