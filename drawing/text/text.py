from pyray import draw_text as _ray_draw_text, DARKGRAY

_rendered_ids = set()

def DrawText(id: str, text: str, x: int, y: int, font_size: int = 20, color = DARKGRAY):
    if isinstance(id, int):
        print("[error]: Value 'id' cannot be int. Only string is allowed.")
        return
    
    _ray_draw_text(text.encode('utf-8'), x, y, font_size, color)
    
    if id not in _rendered_ids:
        print(f"[info]: Text element successfully rendered. ID: {id}")
        _rendered_ids.add(id)
