import os
import tkinter as tk
from .CharacterMap import CharacterMap as CM
from .PixelsCharactersConverter import PixelsCharactersConverter as PCC


class Output:
    def __init__(self, args):
        self.cm = CM(args.font)
        self.converter = PCC(self.cm)
        self.image_format = args.format
        self.source_image_path = args.image[0]
        self.dest_file_path = os.path.basename(
            self.source_image_path).split('.')[0]

        print(self.dest_file_path)

    def export(self):
        characters = self.converter.pixels_to_characters(
            self.source_image_path)

        with open(self.dest_file_path + '.txt', mode='w+', encoding='utf-8') as dest_file:
            for line in characters:
                for char in line:
                    dest_file.write(char)
                dest_file.write('\n')

    def convert(self):
        characters = self.converter.pixels_to_characters(
            self.source_image_path)
        dest_image = self.converter.characters_to_image(characters)
        dest_image.save(self.dest_file_path + '.{}'.format(self.image_format))
