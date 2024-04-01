from random import randint

from mapmaking.box import Box
from mapmaking.direction import Direction
from mapmaking.image import generate_final_image


class Map(list):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self[:] = [[Box(self, x, y) for y in range(self.height)] for x in range(self.width)]

    def get_boxes_around(self, x, y) -> list["Box"]:
        boxes = []
        if x != 0:
            boxes.append(self[x - 1][y])
        if x != self.width - 1:
            boxes.append(self[x + 1][y])
        if y != 0:
            boxes.append(self[x][y - 1])
        if y != self.height - 1:
            boxes.append(self[x][y + 1])
        return boxes

    def get_filled_boxes_around(self, x, y) -> list["Box"]:
        return list(filter(lambda box: len(box.possible_tiles) == 1,
                           self.get_boxes_around(x, y)))

    def get_relative_position_of_given_box(self, box1: "Box", box2: "Box") -> Direction:
        if box1.x == box2.x:
            if box1.y == box2.y + 1:
                return Direction.down
            if box1.y == box2.y - 1:
                return Direction.up
        if box1.y == box2.y:
            if box1.x == box2.x + 1:
                return Direction.left
            if box1.x == box2.x - 1:
                return Direction.right

    def set_random_tile(self):
        self.set_tile(randint(0, self.width - 1), randint(0, self.height - 1))

    def set_tile(self, x: int, y: int) -> None:
        self[x][y].set_random_valid_tile()

    def create_map(self):
        self.set_random_tile()
        while ([box for x in range(self.width) for box in self[x] if box.entropy != 1]):
            generate_final_image(self, self.width, self.height)
            self.update_possible_tiles()
            box_to_update = self.get_smallest_entropy_box()
            self.set_tile(box_to_update.x, box_to_update.y)


    def get_smallest_entropy_box(self) -> "Box":
        boxes = [box for x in range(self.width) for box in self[x] if box.entropy != 1]
        box_entropy_list = [box.entropy for box in boxes]
        index_of_smallest_entropy = box_entropy_list.index(min(box_entropy_list))
        return boxes[index_of_smallest_entropy]


    def update_possible_tiles(self):
        for x in range(self.width):
            for y in range(self.height):
                box = self[x][y]
                if len(box.possible_tiles) == 1:
                    continue
                filled_boxes = self.get_filled_boxes_around(x, y)
                if filled_boxes:
                    for filled_box in filled_boxes:
                        direction = self.get_relative_position_of_given_box(box, filled_box)
                        if direction.value == 0:
                            relative_direction = 2
                        elif direction.value == 1:
                            relative_direction = 3
                        elif direction.value == 2:
                            relative_direction = 0
                        elif direction.value == 3:
                            relative_direction = 1

                        frontier = filled_box.possible_tiles[0].frontier_list[relative_direction]
                        box.update_possible_tiles_from_frontiers(**{direction.name: frontier})
