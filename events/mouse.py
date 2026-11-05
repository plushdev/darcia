from pyray import get_mouse_position, is_mouse_button_pressed, is_mouse_button_down, get_mouse_wheel_move, Vector2

def GetMousePos() -> Vector2:
    return get_mouse_position()

def IsMousePressed(button: int = 0) -> bool:
    return is_mouse_button_pressed(button)

def IsMouseDown(button: int = 0) -> bool:
    return is_mouse_button_down(button)

def GetMouseWheel() -> float:
    return get_mouse_wheel_move()