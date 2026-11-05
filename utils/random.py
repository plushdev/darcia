import random
from .colors import MakeColorFromRGB

def RandomInt(min_val: int, max_val: int) -> int:
    return random.randint(min_val, max_val)

def RandomFloat(min_val: float, max_val: float) -> float:
    return random.uniform(min_val, max_val)

def RandomChoice(choices: list):
    if not choices:
        return None
    return random.choice(choices)

def RandomBool(chance: float = 0.5) -> bool:
    return random.random() < chance

def RandomColor():
    return MakeColorFromRGB(
        random.randint(40, 255),
        random.randint(40, 255),
        random.randint(40, 255)
    )