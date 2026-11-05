import math

def Clamp(value: float, min_val: float, max_val: float) -> float:
    return max(min_val, min(value, max_val))

def Lerp(start: float, end: float, amount: float) -> float:
    return start + (end - start) * Clamp(amount, 0.0, 1.0)

def Distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def DegToRad(degrees: float) -> float:
    return degrees * (math.pi / 180.0)

def RadToDeg(radians: float) -> float:
    return radians * (180.0 / math.pi)

def Approach(current: float, target: float, max_delta: float) -> float:
    if current < target:
        return min(current + max_delta, target)
    elif current > target:
        return max(current - max_delta, target)
    return target