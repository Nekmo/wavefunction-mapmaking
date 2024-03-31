from random import randint, choice

from mapmaking.box import Box
from mapmaking.tiles import TILES_LIST


class Map(list):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self[:] = [[Box(self, x, y) for y in range(self.width)] for x in range(self.height)]

    def boxes_around(self, x, y):
        return [
            self[i][j] for i in range(x - 1, x + 2)
            for j in range(y - 1, y + 2) if 0 <= i < self.height
                                            and 0 <= j < self.width and (i, j) != (x, y)
        ]

    def set_random_tile(self):
        box = self[randint(0, self.height)][randint(0, self.width)]
        box.set_tile(choice(TILES_LIST))
