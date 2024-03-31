from os import listdir
from os.path import isfile, join

from PIL import Image


class Tile:
    def __init__(
            self,
            image,
            frontier_list,
            special='',
    ):
        self.image = image
        self.frontier_list = frontier_list
        self.special = special
        self.possible_rotations = 0 if special else rotations_needed(frontier_list)


    def is_compatible_with(self, other_tile, other_position='up'):
        if other_position == 'up':
            return self.frontier_list[0] == other_tile.frontier_list[2]
        elif other_position == 'down':
            return self.frontier_list[2] == other_tile.frontier_list[0]
        elif other_position == 'right':
            return self.frontier_list[1] == other_tile.frontier_list[3]
        elif other_position == 'left':
            return self.frontier_list[3] == other_tile.frontier_list[1]
        else:
            raise ValueError(f'invalid value for other position: {other_position}')

def frontiers_from_name(fname):
    fname = fname.partition('.')[0]
    frontiers = []
    for ii in range(3):
        _f, _, fname = fname.partition('-')
        frontiers.append(_f)
    if '-' in fname:
        _f, _, special = fname.partition('-')
        frontiers.append(_f)
    else:
        frontiers.append(fname)
        special = ''
    return frontiers, special


def rotate_frontier_list(old_frontier_list):
    new_frontier_list = [_front for _front in old_frontier_list[1:]]
    new_frontier_list.append(old_frontier_list[0])
    return new_frontier_list


def rotations_needed(frontier_list):
    if len(set(frontier_list)) == 1:
        return 0
    if frontier_list[0] == frontier_list[2] and frontier_list[1] == frontier_list[3]:
        return 1
    return 3


def tile_from_file(fname, pathname):
    frontiers, special = frontiers_from_name(fname)
    fpath = join(pathname, fname)
    im = Image.open(fpath)

    newtile = Tile(
        image=im,
        frontier_list=frontiers,
        special=special,
    )
    return newtile


def rotate_tile(oldtile):
    old_frontier_list = oldtile.frontier_list
    new_im = oldtile.image.rotate(-90)
    new_frontier_list = [old_frontier_list[-1]] + [_front for _front in old_frontier_list[:-1]]
    return Tile(
        new_im,
        new_frontier_list,
        special=oldtile.special,
    )

# poner el directorio en tiles para no generarlo cada vez
def create_tile_list(pathname):
    file_list = [f for f in listdir(pathname) if isfile(join(pathname, f))]
    tile_list = []
    for file in file_list:
        new_tile = tile_from_file(file, pathname)
        tile_list.append(new_tile)
        for rotation in range(new_tile.possible_rotations):
            new_tile = rotate_tile(new_tile)
            tile_list.append(new_tile)

    return tile_list
