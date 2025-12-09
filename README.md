# 🎵 Linked List Playlist Manager

A visual and interactive Python application that simulates three fundamental Linked List data structures using a real-world **music playlist manager**.

This project helps students clearly understand **Singly**, **Doubly**, and **Circular** Linked Lists through visualization and user interaction.

---

## 📌 Project Overview  

The Playlist Manager demonstrates how different linked list implementations behave when performing playlist operations:

- Adding songs  
- Removing songs  
- Navigating (Next / Previous)  
- Looping through songs  
- Viewing real-time pointer and node changes  

This tool visually displays:

- 🟦 **Nodes (Songs)**  
- 🔗 **Pointers (next / prev)**  
- 🔄 **Live updates on every operation**  

---

## 🎯 Features  

✅ Supports **three linked list types**  
- Singly  
- Doubly  
- Circular  

✅ Real-time **visual representation**  
✅ Interactive playback & playlist controls  
✅ Step-by-step educational simulation  
✅ Clean and beginner-friendly GUI  
  

---

## 📚 Data Structures Implemented  

### 1️⃣ **Singly Linked List**
- Node points to next only  
- Forward traversal  
- Memory efficient  

### 2️⃣ **Doubly Linked List**
- Node has `next` and `prev` pointers  
- Forward + backward traversal  
- Uses extra memory  

### 3️⃣ **Circular Linked List**
- Last node links back to the first  
- Infinite looping capability  
- Perfect for repeat playlists  

---

## 🎮 How to Use  

1. Run the application  
2. Choose the **Linked List type**  
3. Add songs manually or through **Add Random**  
4. Use playback controls:  
   - ▶ **Play**  
   - ⏭ **Next**  
   - ⏮ **Previous**  
5. Remove selected song or clear playlist  
6. Observe the **real-time visualization** of linked list changes  

---

## 📂 Project Structure  

```text
playlist_manager/
│
├── main.py               # Entry point - RUN THIS FILE
├── README.md             # Project documentation
│
├── data_structures/      # Linked list implementations
│   ├── node.py
│   ├── singly_list.py
│   ├── doubly_list.py
│   └── circular_list.py
│
├── gui/                  # GUI components
│   ├── app.py
│   ├── controls.py
│   └── display.py
│
└── utils/                # Helper utilities
    └── helpers.py
```
---
## 🛠 Technologies Used

### 🔹 Programming Language
- Python 3.x

### 🔹 GUI Framework
- Tkinter (built-in Python library)

### 🔹 Core Computer Science Concepts
- Data Structures  
  - Singly Linked List  
  - Doubly Linked List  
  - Circular Linked List  
- Object-Oriented Programming (OOP)  
- Event Handling  
- GUI Programming  

### 🔹 Development Tools
- Visual Studio Code / PyCharm / Any Python IDE
- Git & GitHub (Version Control)

### 🔹 Dependencies
- No external libraries required  
- Uses only built-in Python packages

---

## ⚙️ Installation

1. **Install Python 3.x**  
   Download from: https://www.python.org/downloads/

2. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/playlist-manager.git

