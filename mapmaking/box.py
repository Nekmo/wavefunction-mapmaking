import os
from random import choice
from typing import TYPE_CHECKING

from mapmaking.direction import Direction
from mapmaking.tiles import create_tile_list

if TYPE_CHECKING:
    from mapmaking.map import Map


class Box:
    def __init__(self, map: "Map", x, y, possible_tiles: list = None):
        self.map = map
        self.x = x
        self.y = y
        if possible_tiles:
            self.possible_tiles = possible_tiles
        else:
            self.possible_tiles = create_tile_list(os.path.join("..", "tiles"))

    def update_possible_tiles_from_frontiers(self, up = None, down = None, left = None, right = None):
        if up:
            self.possible_tiles = [tile for tile in self.possible_tiles if tile.frontier_list[Direction.up.value] == up]
        if right:
            self.possible_tiles = [tile for tile in self.possible_tiles if tile.frontier_list[Direction.right.value] == right]
        if down:
            self.possible_tiles = [tile for tile in self.possible_tiles if tile.frontier_list[Direction.down.value] == down]
        if left:
            self.possible_tiles = [tile for tile in self.possible_tiles if tile.frontier_list[Direction.left.value] == left]
        if not self.possible_tiles:
            raise ValueError('No valid tiles')


    @property
    def entropy(self) -> int:
        return len(self.possible_tiles)

    def set_random_valid_tile(self):
        self.possible_tiles = [choice(self.possible_tiles)]

    def __repr__(self):
        return f"Box<{self.possible_tiles[0]}>"
