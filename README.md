# darcia 
**Current Version:** `v0.04.0`
> 🚨 **Attention!**
> The engine is currently in **Alpha Testing**. This means you can expect **frequent updates and continuous, intensive code improvements**. Always pull the latest changes to stay on the most up-to-date version!

---

## Features

- **Code Simplicity:** Intuitive and straightforward API designed to let you jump straight into game development without unnecessary boilerplate or complex setups.
- **High Performance:** Powered by Python and Raylib (`pyray`) to deliver lightning-fast 2D rendering and silky-smooth execution.
- **Clean Codebase:** Meticulously structured, lightweight, and readable code that is easy to understand, maintain, and extend.

---

## How to Install / Setup

Getting **darcia** into your project is simple:

1. **Clone or Download** this repository as a ZIP archive and extract it.
2. Copy the `darcia` folder into the root directory of your own project:
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
After this, your Project Directory will look like this:
```text
your_game_project/
├── darcia/
│   ├── core/
│   ├── drawing/
│   ├── events/
│   └── ...
└── main.py
```


## How to Use?

Getting started with **darcia** is super easy! Here is a minimal setup example:

```python
from darcia.core.window import Window
from darcia.drawing.text.text import DrawText

def main():
    # 1. Create the engine window
    win = Window(title="darcia", width=800, height=600, fps_limit=60)

    # 2. Define your game loop
    def game_loop():
        DrawText("hello_txt", "Welcome to darcia!", 250, 280, 20)

    # 3. Run the game!
    win.run(draw_callback=game_loop)

if __name__ == "__main__":
    main()
```
---

## Want to Leave Feedback?

Have an idea, found a bug, or just want to chat about the engine? 
Reach out on Discord anytime: **`@mrplushieds`**!
