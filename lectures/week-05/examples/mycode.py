from compas.geometry import Point, Box

class Room:
    def __init__(self, name, height, color):
        self.name = name
        self.height = height
        self.color = color

    def paint(self, new_color):
        self.color = new_color

    def draw(self, x, y):
        corner1 = Point(x, y, 0)
        corner2 = Point(x + 1, y + 1, 0)
        box = Box.from_corner_corner_height(corner1, corner2, self.height / 100)
        return box