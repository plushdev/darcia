class PhysicBody:
    def __init__(self, x: float, y: float, width: float, height: float, mass: float = 1.0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx = 0.0
        self.vy = 0.0
        self.mass = mass
        self.is_grounded = False

    def update(self, dt: float, gravity: float = 900.0, ground_y: float = 600.0, use_ground: bool = True):
        self.vy += gravity * dt
        
        self.x += self.vx * dt
        self.y += self.vy * dt
        
        if use_ground:
            if self.y + self.height >= ground_y:
                self.y = ground_y - self.height
                self.vy = 0.0
                self.is_grounded = True
            else:
                self.is_grounded = False
        else:
            self.is_grounded = True

    def jump(self, force: float = -400.0):
        if self.is_grounded:
            self.vy = force
