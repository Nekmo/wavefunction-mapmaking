from random import choice

from PIL import Image


def generate_final_image(map: list[list], width: int, height: int):
    final_image = Image.new('RGB', (width * 64, height * 64))
    for x, box_row in enumerate(map):
        for y, box in enumerate(box_row):
            if len(box.possible_tiles) != 1:
                continue
            tile = box.possible_tiles[0]
            image = tile.image
            """
                2 0 -> 0 0
                1 0 -> 64 0
                0 
            
            
                0 0 -> 0 128
                0 1 -> 0 64
                0 2 -> 0 0
                1 0 -> 64 128
                1 1 -> 64 64
                1 2 -> 64 0
            """
            final_image.paste(image, (convert_x(x),convert_y(y)))

    final_image.save('final_image.png', 'JPEG')

def convert_x(x:int):
    return x * 64

def convert_y(y:int):
    return (2-y) * 64
