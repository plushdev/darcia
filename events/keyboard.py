from pyray import is_key_down, is_key_pressed, is_key_released

def IsKeyDown(key: int) -> bool:
    return is_key_down(key)

def IsKeyPressed(key: int) -> bool:
    return is_key_pressed(key)

def IsKeyReleased(key: int) -> bool:
    return is_key_released(key)
