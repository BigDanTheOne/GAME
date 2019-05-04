from strategy import *


class BBox:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.r = radius
    def intersect(self, point):
        return ((self.x - point[0]) ** 2 + (self.y - point[1]) ** 2) ** (0.5) <= self.radius

class Unit:
    # imgHeadad':  pygame.Surface
    # imgBody:  pygame.Surface
    # bbox: BBox(100, 100, 10)
    # speed: int = unitSpeed

    # def __init__(self, imgHead, imgBody):
    #     self.imgHead = pygame.image.load(imgHead)
    #     self.imgBody = pygame.image.load(imgBody)

    def step(self, target, delta_t):
        new_bbox = copy.deepcopy(self.bbox)
        new_bbox.x += self.speed * math.sin(
            math.atan2(self.target[0] - self.bbox.x,
                       self.target[1] - self.bbox.y)) * delta_t
        new_bbox.y += self.speed * math.cos(
            math.atan2(self.target[0] - self.bbox.x,
                       self.target[1] - self.bbox.y)) * delta_t
        self.bbox = new_bbox

    hit = hit1

    def move(self, target, delta_t):
        pass

    def death(self):
        pass
