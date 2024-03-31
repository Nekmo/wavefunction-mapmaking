import os.path
import unittest

from PIL.Image import Image

from mapmaking.tiles import Tile, frontiers_from_name, rotate_frontier_list, is_simmetric, rotations_needed, \
    tile_from_file, rotate_tile, create_tile_list


class TileTests(unittest.TestCase):
    tile_path = os.path.join("..", "tiles")

    def test_frontiers_from_name(self):
        frontiers, special = frontiers_from_name("a-a-a-a.jpg")

        assert special == ""
        assert frontiers == ["a", "a", "a", "a"]

    def test_frontiers_from_name_with_special_tile(self):
        frontiers, special = frontiers_from_name("a-t-a-t-istmo.jpg")

        assert special == "istmo"
        assert frontiers == ["a", "t", "a", "t"]

    def test_frontiers_from_name_with_fractioned_frontier(self):
        frontiers, special = frontiers_from_name("t-t-ta-at.jpg")

        assert special == ""
        assert frontiers == ["t", "t", "ta", "at"]

    def test_rotate_frontier_list(self):
        frontier_list = ["a", "t", "a", "t"]
        new_frontier_list = rotate_frontier_list(frontier_list)

        assert new_frontier_list == ["t", "a", "t", "a"]

    def test_rotations_needed(self):
        assert rotations_needed(["a", "t", "at", "ta"]) == 3
        assert rotations_needed(["a", "a", "a", "a"]) == 0
        assert rotations_needed(["a", "t", "t", "t"]) == 3
        assert rotations_needed(["a", "t", "a", "t"]) == 1
        assert rotations_needed(["t", "a", "t", "t"]) == 3


    def test_tile_from_file(self):
        tile = tile_from_file("a-a-a-a.jpg", self.tile_path)
        assert isinstance(tile, Tile)
        assert tile.possible_rotations == 0

    def test_tile_from_file_special(self):
        tile = tile_from_file("a-a-a-a-ballena.jpg", self.tile_path)
        assert isinstance(tile, Tile)
        assert tile.possible_rotations == 0

    def test_rotate_tile(self):
        tile = tile_from_file("t-a-a-a.jpg", self.tile_path)
        rotated_tile = rotate_tile(tile)

        # esta bien?
        assert rotated_tile.image_list[0] != tile.image_list[0]
        # assert rotated_tile.image_list[0].rotate(-90) == tile.image_list[0]

    # def test_tile(self):
    #     im = Image.open('')
    #     frontiers, special = frontiers_from_name("")
    #     tile = Tile(im, frontiers, special)
