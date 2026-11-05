from pyray import draw_line, draw_line_ex, Vector2, BLACK

_rendered_ids = set()

def DrawLine(id: str, x1: int, y1: int, x2: int, y2: int, thickness: float = 1.0, color = BLACK):
    if isinstance(id, int):
        print("[error]: Value 'id' cannot be int. Only string is allowed.")
        return
    
    if thickness > 1.0:
        start_pos = Vector2(x1, y1)
        end_pos = Vector2(x2, y2)
        draw_line_ex(start_pos, end_pos, thickness, color)
    else:
        draw_line(x1, y1, x2, y2, color)
        
    if id not in _rendered_ids:
        print(f"[info]: Line element successfully rendered. ID: {id}")
        _rendered_ids.add(id)