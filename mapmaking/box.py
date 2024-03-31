import os
from random import choice
from typing import TYPE_CHECKING

from mapmaking.tiles import create_tile_list

if TYPE_CHECKING:
    from mapmaking.map import Map


class Box:
    def __init__(self, map: "Map", x, y):
        self.map = map
        self.x = x
        self.y = y
        self.possible_tiles = create_tile_list(os.path.join("..", "tiles"))

    def get_boxes_around(self) -> list["Box"]:
        return self.map.boxes_around(self.x, self.y)

    def get_filled_boxes_around(self) -> list["Box"]:
        return list(filter(lambda box: len(box.possible_tiles) == 1,
                           self.get_boxes_around()))

    @property
    def entropy(self) -> int:
        return len(self.possible_tiles)

    def update_entropy_around(self):
        boxes_around = self.get_boxes_around()
        for box in boxes_around:
            box.update_possible_tiles_around()

    def set_tile(self, tile):
        self.possible_tiles = [tile]
        self.update_possible_tiles_around()

    def set_random_tile(self):
        self.set_tile(choice(self.possible_tiles))

    def get_smallest_entropy_box(self, boxes: ["Box"]) -> "Box":
        for box in boxes:
            box.update_possible_tiles()
        box_entropy_list = [box.entropy for box in boxes]
        index_of_smallest_entropy = box_entropy_list.index(min(box_entropy_list))
        return boxes[index_of_smallest_entropy]

    def update_possible_tiles_around(self):
        if len(self.possible_tiles) == 1:
            return
        smallest_entropy_box = self.get_smallest_entropy_box(self.get_boxes_around())
        smallest_entropy_box.update_possible_tiles()
        smallest_entropy_box.set_random_tile()

    def update_possible_tiles(self):
        boxes_around = self.get_filled_boxes_around()
        for box in boxes_around:
            relative_position = self.map.get_relative_position_of_given_box(self, box)
            other_tile = box.possible_tiles[0]
            # TODO Esto resetea la lista de tiles posibles en vez de conservar restricciones anteriores
            self.possible_tiles = [tile for tile in create_tile_list("tiles") if
                                   other_tile.is_compatible_with(tile, relative_position)]

    def __repr__(self):
        return f"Box<{self.possible_tiles[0]}>"
