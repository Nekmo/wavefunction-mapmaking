from mapmaking.image import generate_final_image
from mapmaking.map import Map

import click


@click.command()
@click.option('--width', default=12, help='Width.')
@click.option('--height', default=8, help='Height.')
def create_map(width, height):
    """Create a map."""
    map = Map(width, height)
    map.set_random_tile()
    print(map)
    generate_final_image(map, map.width, map.height)


if __name__ == '__main__':
    create_map()
