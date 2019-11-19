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
        # if mode == CharacterMap.LucidaSansConsole() or mode is None:
        return ['Q', 'W', 'M', 'B', 'N', 'D', 'R', 'O', 'G', 'H', 'E',
                'K', 'A', 'P', 'U', 'S', 'X', 'Z', 'V', 'C', 'I', 'F', 'Y', 'T', 'J', 'L']

    def __threshold(self, mode=None):
        interval = 0
        threshold_list = []

        if mode == CharacterMap.LucidaSansConsole() or mode is None:
            interval = 255/len(self.character_map)

        for i in range(0, len(self.character_map)):
            result = math.floor(0 + interval * i)
            threshold_list.append(result)

        return threshold_list

    def __font(self, mode=None):
        path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'fonts'))
        if mode == CharacterMap.LucidaSansConsole() or mode is None:
            return os.path.join(path, 'lucon.ttf'), -1
        elif mode == CharacterMap.Braciola():
            return os.path.join(path, 'braciola.ttf'), 0

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
        return 'bruciola'
