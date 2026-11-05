from pyray import draw_rectangle, get_screen_width, get_screen_height, draw_texture_pro, Rectangle, Vector2, WHITE
from darcia.utils.spriteloader import LoadSprite

_rendered_ids = set()

def DrawBackgroundViaColor(id: str, color : WHITE):
    if isinstance(id, int):
        print("[error]: Value 'id' cannot be int. Only string is allowed.")
        return
    
    width = get_screen_width()
    height = get_screen_height()
    
    draw_rectangle(0, 0, width, height, color)
        
    if id not in _rendered_ids:
        print(f"[info]: Background element successfully rendered. ID: {id}")
        _rendered_ids.add(id)

def DrawBackgroundViaSprite(id: str, sprite_path: str):
    if isinstance(id, int):
        print("[error]: Value 'id' cannot be int. Only string is allowed.")
        return
    
    texture = LoadSprite(sprite_path)
    if not texture:
        return
    
    width = get_screen_width()
    height = get_screen_height()
    
    source_rec = Rectangle(0, 0, texture.width, texture.height)
    dest_rec = Rectangle(0, 0, width, height)
    origin = Vector2(0, 0)
    
    draw_texture_pro(texture, source_rec, dest_rec, origin, 0.0, WHITE)
        
    if id not in _rendered_ids:
        print(f"[info]: Background sprite element successfully rendered. ID: {id}")
        _rendered_ids.add(id)
