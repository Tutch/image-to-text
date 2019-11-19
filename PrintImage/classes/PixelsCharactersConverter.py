import math
from PIL import Image, ImageDraw, ImageFont


class PixelsCharactersConverter:
    def __init__(self, character_map=None):
        self.character_map = character_map

    def pixels_to_characters(self, source_image_path):
        source_image = Image.open(
            source_image_path, mode='r').convert(mode='L')
        source_image_width = source_image.width
        source_image_height = source_image.height

        char_list = []

        for pixelY in range(source_image_height):
            char_line = []
            for pixelX in range(source_image_width):
                grey_tone = source_image.getpixel((pixelX, pixelY))
                char_line.append(self.character_map.get_character(grey_tone))
            char_list.append(char_line)
        return char_list

    def characters_to_image(self, characters):
        output_text = ''
        scale = 3

        # Width and height based on the elements in the array
        character_count_width = len(characters[0])
        character_count_height = len(characters)

        # Calculating sizes based on scale
        target_width = character_count_width * scale

        font_size = math.ceil(
            (target_width / character_count_width) * 1.666666)
        font_size = 2 if font_size < 2 else font_size

        target_height = math.ceil(
            (target_width/character_count_width) * character_count_height)

        # Preparing dest image
        dest_image = Image.new(mode='L', size=(
            target_width, target_height), color=(255))
        draw = ImageDraw.Draw(dest_image)

        font = ImageFont.truetype(
            font=self.character_map.font, size=font_size, encoding='utf-8')

        for line in characters:
            joined_line = ''.join(line)
            output_text += '{}\n'.format(joined_line)

        # Offsetting characters based on the font
        draw.multiline_text((0, 0),
                            output_text, font=font, align="left", spacing=self.character_map.spacing_offset)

        return dest_image
