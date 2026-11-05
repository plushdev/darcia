from pyray import get_mouse_position, is_mouse_button_pressed, MOUSE_BUTTON_LEFT, LIGHTGRAY, DARKGRAY, GRAY
from ..drawing.geometry.rect import DrawRect
from ..drawing.text.text import DrawText

class Button:
    def __init__(self, id: str, x: int, y: int, width: int, height: int, text: str, roundness: float = 0.25, color = LIGHTGRAY, text_color = DARKGRAY):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.roundness = roundness
        self.color = color
        self.text_color = text_color

    def draw(self) -> bool:
        mouse = get_mouse_position()
        
        is_hovered = (
            self.x <= mouse.x <= self.x + self.width and
            self.y <= mouse.y <= self.y + self.height
        )
        
        current_color = GRAY if is_hovered else self.color
        
        DrawRect(f"{self.id}_bg", self.x, self.y, self.width, self.height, self.roundness, current_color)
        DrawText(f"{self.id}_txt", self.text, self.x + 25, self.y + 15, 20, self.text_color)
        
        if is_hovered and is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
            print(f"[info]: Button '{self.id}' was clicked.")
            return True
            
        return False
