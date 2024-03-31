import os
from random import randint, choice
from typing import Literal

from mapmaking.box import Box
from mapmaking.tiles import create_tile_list


class Map(list):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self[:] = [[Box(self, x, y) for y in range(self.width)] for x in range(self.height)]

    def boxes_around(self, x, y):
        boxes = []
        if x != 0:
            boxes.append(self[x- 1][y])
        if x != self.width - 1:
            boxes.append(self[x + 1][y])
        if y != 0:
            boxes.append(self[x][y-1])
        if y != self.height - 1:
            boxes.append(self[x][y+1])

        return boxes

    def get_relative_position_of_given_box(self, box1: "Box", box2: "Box") -> Literal["down", "up", "left", "right"]:
        if box1.x == box2.x:
            if box1.y == box2.y + 1:
                return "down"
            if box1.y == box2.y - 1:
                return "up"
        if box1.y == box2.y:
            if box1.x == box2.x + 1:
                return "left"
            if box1.x == box2.x - 1:
                return "right"
        pass

    def set_random_tile(self):
        box = self[randint(0, self.height)][randint(0, self.width)]
        box.set_tile(choice(create_tile_list(os.path.join("..", "tiles"))))
