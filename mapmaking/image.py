from random import choice

from PIL import Image


def generate_final_image(map: list[list], width: int, height: int):
    final_image = Image.new('RGB', (width * 64, height * 64))
    for x, box_row in enumerate(map):
        for y, box in enumerate(box_row):
            tile = box.possible_tiles[0]
            image = choice(tile.image_list)
            final_image.paste(image, (y * 64, x * 64))

    final_image.save('final_image.png', 'JPEG')
