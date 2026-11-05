def MoveForward(y: float, speed: float, dt: float) -> float:
    return y - (speed * dt)

def MoveBackward(y: float, speed: float, dt: float) -> float:
    return y + (speed * dt)

def MoveLeft(x: float, speed: float, dt: float) -> float:
    return x - (speed * dt)

def MoveRight(x: float, speed: float, dt: float) -> float:
    return x + (speed * dt)