from pyray import draw_circle, draw_circle_lines, LIGHTGRAY

_rendered_ids = set()

def DrawCircle(id: str, x: int, y: int, radius: float, color = LIGHTGRAY, filled: bool = True):
    if isinstance(id, int):
        print("[error]: Value 'id' cannot be int. Only string is allowed.")
        return
    
    if filled:
        draw_circle(int(x), int(y), radius, color)
    else:
        draw_circle_lines(int(x), int(y), radius, color)
        
    if id not in _rendered_ids:
        print(f"[info]: Circle element successfully rendered. ID: {id}")
        _rendered_ids.add(id)
