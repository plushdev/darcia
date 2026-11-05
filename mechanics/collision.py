from pyray import (
    Rectangle, 
    Vector2,
    check_collision_recs,
    check_collision_circles,
    check_collision_point_rec,
    check_collision_point_circle
)

def BoxCollision(x1: float, y1: float, w1: float, h1: float, x2: float, y2: float, w2: float, h2: float) -> bool:
    rec1 = Rectangle(x1, y1, w1, h1)
    rec2 = Rectangle(x2, y2, w2, h2)
    return check_collision_recs(rec1, rec2)

def CircleCollision(x1: float, y1: float, r1: float, x2: float, y2: float, r2: float) -> bool:
    center1 = Vector2(x1, y1)
    center2 = Vector2(x2, y2)
    return check_collision_circles(center1, r1, center2, r2)

def CheckBoxCollision(px: float, py: float, rx: float, ry: float, rw: float, rh: float) -> bool:
    point = Vector2(px, py)
    rec = Rectangle(rx, ry, rw, rh)
    return check_collision_point_rec(point, rec)

def CheckCircleCollision(px: float, py: float, cx: float, cy: float, cr: float) -> bool:
    point = Vector2(px, py)
    center = Vector2(cx, cy)
    return check_collision_point_circle(point, center, cr)