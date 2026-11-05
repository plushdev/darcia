from pyray import load_texture

_textures = {}

def LoadSprite(texture_path: str):
    if texture_path in _textures:
        return _textures[texture_path]
    
    try:
        texture = load_texture(texture_path)
        _textures[texture_path] = texture
        print(f"[info]: Sprite successfully loaded: {texture_path}")
        return texture
    except Exception as e:
        print(f"[error]: Failed to load sprite from {texture_path}: {e}")
        return None