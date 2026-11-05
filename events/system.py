from pyray import is_window_resized, get_frame_time

def IsResized() -> bool:
    return is_window_resized()

def DeltaTime() -> float:
    return get_frame_time()