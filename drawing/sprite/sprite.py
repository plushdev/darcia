from pyray import Rectangle, Vector2, WHITE, draw_texture_pro

def ApplySpriteToObject(obj, sprite_name: str):
    obj.sprite_name = sprite_name
    return obj.sprite_name

def SetSpriteTint(obj, r: int, g: int, b: int, a: int = 255):
    obj.sprite_tint = (r, g, b, a)

def FlipSprite(obj, flip_x: bool = False, flip_y: bool = False):
    obj.flip_x = flip_x
    obj.flip_y = flip_y
