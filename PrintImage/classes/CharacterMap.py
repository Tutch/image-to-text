import math
import os


class CharacterMap:

    def __init__(self, mode=None):
        if mode is None:
            print('Defaulting to Lucida...')
            mode = CharacterMap.LucidaSansConsole()

        self.character_map = self.__map(mode)
        self.threshold_map = self.__threshold(mode)
        self.font, self.spacing_offset = self.__font(mode)

    def __map(self, mode=None):
        # This mapping was created for Lucida. The first character in the
        # list has more "pixels per square" than the second one, the second has more than
        # the third etc so it works like a "grayscale" of sorts.
        # TODO: Create a mapping for Braciola and other potential fonts.
        return ['Q', 'W', 'M', 'B', 'N', 'D', 'R', 'O', 'G', 'H', 'E',
                'K', 'A', 'P', 'U', 'S', 'X', 'Z', 'V', 'C', 'I', 'F', 'Y', 'T', 'J', 'L']

    def __threshold(self, mode=None):
        interval = 0
        threshold_list = []

        interval = 255/len(self.character_map)

        for i in range(0, len(self.character_map)):
            result = math.floor(0 + interval * i)
            threshold_list.append(result)

        return threshold_list

    def __font(self, mode=None):
        path = os.path.abspath(os.path.join(os.path.dirname(
            os.path.realpath(__file__)), '..', 'fonts'))
        if mode == CharacterMap.LucidaSansConsole() or mode is None:
            return os.path.join(path, 'lucon.ttf'), -3
        elif mode == CharacterMap.Braciola():
            return os.path.join(path, 'braciola.ttf'), -3

    def get_character(self, pixel_color):
        if self.character_map is not None and self.threshold_map is not None:
            i = len(self.character_map)-1
            for value in reversed(self.threshold_map):
                if pixel_color >= value:
                    return self.character_map[i]
                i -= 1

    @staticmethod
    def LucidaSansConsole():
        return 'lucida'

    @staticmethod
    def Braciola():
        return 'braciola'
