import unittest

from mapmaking.box import Box
from mapmaking.tiles import Tile


class MyTestCase(unittest.TestCase):
    def test_update_possible_tiles_from_frontiers(self):
        earth_tile = Tile(None, ["t", "t", "t", "t"])
        box = Box(None, 1, 1,
                  [Tile(None, ["a", "a", "a", "a"]),
                   earth_tile
                   ])
        box.update_possible_tiles_from_frontiers(up="t")

        self.assertEqual(len(box.possible_tiles), 1)
        self.assertIs(box.possible_tiles[0], earth_tile)

    def test_update_possible_tiles_from_frontiers_with_more_possible_tiles(self):
        tile1 = Tile(None, ["t", "t", "t", "t"])
        tile2 = Tile(None, ["t", "t", "t", "ta"])
        tile3 = Tile(None, ["t", "t", "at", "ta"])
        tile4 = Tile(None, ["t", "t", "a", "ta"])

        tile5 = Tile(None, ["a", "a", "a", "a"])
        tile6 = Tile(None, ["a", "a", "t", "a"])
        box = Box(None, 1, 1,
                  [tile1, tile2, tile3, tile4, tile5, tile6])
        box.update_possible_tiles_from_frontiers(up="t")

        self.assertEqual(len(box.possible_tiles), 4)
        self.assertIs(box.possible_tiles[0], tile1)
        self.assertIs(box.possible_tiles[1], tile2)
        self.assertIs(box.possible_tiles[2], tile3)
        self.assertIs(box.possible_tiles[3], tile4)

    def test_update_possible_tiles_from_frontiers_with_even_more_possible_tiles(self):
        tile1 = Tile(None, ["t", "t", "t", "t"])
        tile2 = Tile(None, ["t", "t", "t", "ta"])
        tile4 = Tile(None, ["t", "t", "a", "ta"])
        tile5 = Tile(None, ["a", "a", "a", "a"])
        tile6 = Tile(None, ["a", "a", "t", "a"])

        tile3 = Tile(None, ["t", "a", "at", "ta"])

        box = Box(None, 1, 1,
                  [tile1, tile2, tile3, tile4, tile5, tile6])
        box.update_possible_tiles_from_frontiers(up="t", right="a", down="at", left="ta")

        self.assertEqual(len(box.possible_tiles), 1)
        self.assertIs(box.possible_tiles[0], tile3)
