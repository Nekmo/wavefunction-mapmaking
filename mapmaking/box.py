from typing import Optional, Literal

from mapmaking.map import Map


class Box:
    def __init__(self, map: "Map", x, y):
        self.map = map
        self.x = x
        self.y = y
        self.possible_tiles = []

    def get_boxes_around(self) -> list["Box"]:
        return self.map.boxes_around(self.x, self.y)

    def get_number_of_boxes_around(self) -> int:
        return len(self.get_boxes_around())

    def get_filled_boxes_around(self) -> list["Box"]:
        return list(filter(lambda box: all(len(box.possible_tiles) == 1) ,self.get_boxes_around()))

    def get_relative_position_of_given_box(self, box: "Box") -> Literal["down", "up", "left", "right"]:
        if self.x == box.x:
            if self.y == box.y + 1:
                return "down"
            if self.y == box.y - 1:
                return "up"
        if self.y == box.y:
            if self.x == box.x + 1:
                return "left"
            if self.x == box.x - 1:
                return "right"

    @property
    def entropy(self) -> Optional[int]:
        # primero calcula con 8 box colindantes
        # luego calcula bordes
        boxes_around = self.get_filled_boxes_around()
        self.possible_tiles = # create_tile_list()
        for box in boxes_around:
            # check up
            relative_position = self.get_relative_position_of_given_box(box)
            other_tile = box.possible_tiles[0]
            for possible_tiles in self.possible_tiles:
                list(map(lambda is_possible: ))



        if len(self.possible_tiles) == 0:
            return None
        return len(self.possible_tiles)

    def update_entropy_around(self):
        boxes_around = self.get_boxes_around()
        for box in boxes_around:
            box.update_possible_tiles_around()

    def set_tile(self, tile):
        self.possible_tiles = [tile]
        self.update_possible_tiles_around()

    def update_possible_tiles_around(self):
        for box in self.get_boxes_around():
            box.update_possible_tiles()

    def update_possible_tiles(self):
        for