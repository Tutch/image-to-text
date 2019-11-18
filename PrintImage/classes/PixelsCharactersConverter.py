import math
from PIL import Image, ImageDraw, ImageFont
from .CharacterMap import CharacterMap as CM


class PixelsCharactersConverter:
    def __init__(self):
        pass

    def pixels_to_characters(self, source_image_path):
        source_image = Image.open(
            source_image_path, mode='r').convert(mode='L')
        source_image_width = source_image.width
        source_image_height = source_image.height

        cm = CM()

        char_list = []

        for pixelY in range(source_image_height):
            char_line = []
            for pixelX in range(source_image_width):
                grey_tone = source_image.getpixel((pixelX, pixelY))
                char_line.append(cm.get_character(grey_tone))
            char_list.append(char_line)
        return char_list

    def characters_to_image(self, characters):
        character_count_width = len(characters[0])
        character_count_height = len(characters)
        target_width = 1920
        font_size = math.ceil(target_width / (character_count_width * 2))
        font_size = 2 if font_size < 2 else font_size
        actual_width = font_size * character_count_width * 2
        actual_height = math.ceil(
            (actual_width/character_count_width) * character_count_height)

        dest_image = Image.new(mode='L', size=(
            actual_width, actual_height), color=(255))
        draw = ImageDraw.Draw(dest_image)
        font = ImageFont.truetype('lucon.ttf', font_size, encoding='utf-8')

        line_count = 1

        for line in characters:
            joined_line = ' '.join(line)
            draw.text((0, font_size * line_count),
                      joined_line, font=font, align="left")
            line_count += 1

        return dest_image
