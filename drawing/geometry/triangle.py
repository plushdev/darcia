from pyray import draw_triangle, draw_triangle_lines, Vector2, LIGHTGRAY

_rendered_ids = set()

def DrawTriangle(id: str, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, color = LIGHTGRAY, filled: bool = True):
    if isinstance(id, int):
        print("[error]: Value 'id' cannot be int. Only string is allowed.")
        return
    
    v1 = Vector2(x1, y1)
    v2 = Vector2(x2, y2)
    v3 = Vector2(x3, y3)
    
    if filled:
        draw_triangle(v1, v2, v3, color)
    else:
        draw_triangle_lines(v1, v2, v3, color)
        
    if id not in _rendered_ids:
        print(f"[info]: Triangle element successfully rendered. ID: {id}")
        _rendered_ids.add(id)