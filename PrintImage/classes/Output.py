import tkinter as tk
from .CharacterMap import CharacterMap as CM
from .PixelsCharactersConverter import PixelsCharactersConverter as PCC


class Output:
    @staticmethod
    def export(source_image_path, dest_file_path):
        cm = CM()
        converter = PCC(cm)
        characters = converter.pixels_to_characters(source_image_path)

        with open(dest_file_path, mode='w+', encoding='utf-8') as dest_file:
            for line in characters:
                for char in line:
                    dest_file.write(char)
                dest_file.write('\n')

    @staticmethod
    def convert(source_image_path, dest_image_path):
        #cm = CM(CM.LucidaSansConsole())
        cm = CM(CM.Braciola())
        converter = PCC(cm)
        characters = converter.pixels_to_characters(source_image_path)
        dest_image = converter.characters_to_image(characters)
        dest_image.save(dest_image_path)
