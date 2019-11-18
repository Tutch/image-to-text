from .PixelsCharactersConverter import PixelsCharactersConverter as PCC
import tkinter as tk


class Output:
    @staticmethod
    def export(source_image_path, dest_file_path):
        converter = PCC()
        characters = converter.pixels_to_characters(source_image_path)

        with open(dest_file_path, mode='w+', encoding='utf-8') as dest_file:
            for line in characters:
                for char in line:
                    dest_file.write(char)
                dest_file.write('\n')

    @staticmethod
    def convert(source_image_path, dest_image_path):
        converter = PCC()
        characters = converter.pixels_to_characters(source_image_path)
        dest_image = converter.characters_to_image(characters)
        dest_image.save('output.png')
