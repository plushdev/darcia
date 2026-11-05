from pyray import draw_rectangle, draw_rectangle_rounded, Rectangle, LIGHTGRAY

_rendered_ids = set()

def DrawRect(id: str, x: int, y: int, width: int, height: int, roundness: float = 0.0, color = LIGHTGRAY):
    if isinstance(id, int):
        print("[error]: Value 'id' cannot be int. Only string is allowed.")
        return
    
    if roundness > 0.0:
        rec = Rectangle(x, y, width, height)
        draw_rectangle_rounded(rec, roundness, 4, color)
    else:
        draw_rectangle(x, y, width, height, color)
        
    if id not in _rendered_ids:
        print(f"[info]: Rectangle element successfully rendered. ID: {id}")
        _rendered_ids.add(id)