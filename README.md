# 🌐 FlyNetX: Terminal Cat

![FlyNetX](FlyNetX.jpg)

**Terminal Cat** is a proprietary, multi-threaded communication uplink developed by **FlyNetX**. Designed with a sleek, neon-cyan cyberpunk aesthetic, this terminal-based application allows multiple operatives (Runners) to "jack into" a centralized mainframe and broadcast encrypted messages in real-time across the grid.

---

## ⚡ Features

* **Multi-Threaded Architecture:** Handles concurrent bi-directional communication seamlessly. You can type while receiving incoming broadcasts without terminal scrambling.
* **Cyberpunk UI:** High-contrast neon cyan ANSI color grading for that authentic deck-runner feel.
* **Centralized Mainframe:** Lightweight server script handles client broadcasting and connection stability.
* **Graceful Disconnects:** Catch connection drops and `/exit` commands cleanly without crashing the grid.

---

## 🛠 Prerequisites

* **Python 3.7+**
* **Colorama** (Required for Windows users to properly render ANSI neon color codes)

To install the required dependencies, run:
```bash
pip install colorama
```

---

## 🚀 Boot Sequence (How to Run)

### 1. Initialize the Mainframe (Server)
The mainframe must be brought online before any agents can connect. Open your terminal and run:

```bash
python server.py
```
*Wait for the `[FlyNetX SYSTEM] Mainframe online on port 65432. Awaiting connections...` prompt.*

### 2. Jack In (Client)
Launch the **Terminal Cat** client. You can open as many terminal windows as you want to simulate multiple users. 

```bash
python client.py
```
*   Enter your **Agent Alias** when prompted.
*   You are now connected to the grid. Start typing to broadcast.

---

## ⌨️ System Commands

* `/exit` : Gracefully sever your connection to the mainframe and exit the application.
* `Ctrl + C` : Initiate an emergency disconnect (Hard abort).

---

## 📂 Grid Architecture (Project Structure)

```text
FlyNetX_Terminal_Cat/
│
├── server.py        # The Mainframe: handles socket binding, listening, and broadcasting.
├── client.py        # The Deck: handles server connection, threading, and UI rendering.
├── FlyNetX.jpg      # Official FlyNetX Organization Logo
└── README.md        # System Documentation
```

---

## 🛡 Security & Lore 

**CONFIDENTIALITY NOTICE:** 
This software is property of the FlyNetX corporation. Unauthorized distribution, decompilation, or tampering with the mainframe socket protocols will result in immediate neural feedback loops and corporate termination. 

*Stay safe on the grid, Runner.*
