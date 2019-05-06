class GoTo:
    def __init__(self, x, y, unit):
        self.x = x
        self.y = y
        self.unit = unit


class SelectUnit:
    def __init__(self, unit):
        self.unit = unit


class Exit:
    pass