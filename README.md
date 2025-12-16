# 🧮 Python Dark-Mode Calculator

A sleek, desktop-based Calculator application built with **Python** and **Tkinter**.

This project demonstrates a robust GUI application structure using **Object-Oriented Programming (OOP)** principles. It features a modern dark theme, full keyboard support, and memory storage functions.

![Calculator Screenshot](screenshot.png)

## ✨ Features

- **Standard Operations:** Addition, Subtraction, Multiplication, Division.
- **Memory Functions:**
  - `M+`: Add current result to memory.
  - `M-`: Subtract current result from memory.
  - `MR`: Recall value from memory to display.
- **Keyboard Support:** \* Full Numpad support.
  - `Enter` to calculate.
  - `Esc` to clear.
  - `Backspace` to delete the last digit.
- **Robust UI:** \* **Dark Mode** theme (#121212) for reduced eye strain.
  - **Read-only Display:** Prevents invalid text entry while allowing programmatic updates.
  - **Error Handling:** Gracefully handles invalid expressions (e.g., Division by Zero).

## 🛠️ Technical Implementation

The application is built using a class-based structure (`Calculator` class) to ensure code modularity and state management.

- **Language:** Python 3.10+
- **GUI Framework:** Tkinter (Standard Library)
- **Architecture:** Object-Oriented (encapsulating state like `self.memory` and UI components).
- **Input Handling:** Event binding (`<Key>`) for physical keyboard integration.

## 🚀 How to Run

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/your-username/calculator-project.git](https://github.com/your-username/calculator-project.git)
    cd calculator-project
    ```

2.  **Run the application:**
    ```bash
    python calculator.py
    ```

## 🕹️ Controls

| Button          | Action           | Keyboard Shortcut            |
| :-------------- | :--------------- | :--------------------------- |
| **0-9**         | Enter numbers    | `0` - `9` (Numpad supported) |
| **+, -, \*, /** | Operators        | `+`, `-`, `*`, `/`           |
| **=**           | Calculate Result | `Enter`                      |
| **C**           | Clear All        | `Esc`                        |
| **<-**          | Backspace        | `Backspace`                  |

## 🔮 Future Improvements

- [ ] Refactor `eval()` to a safer expression parser for security.
- [ ] Add a "History" side-panel to view previous calculations.
- [ ] Add Scientific functions (sin, cos, tan).
- [ ] Package as a standalone `.exe` using PyInstaller.

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
