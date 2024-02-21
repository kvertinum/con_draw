from typing import Tuple


class Canvas:
    def __init__(self, size: Tuple[int, int], char: str):
        self.width, self.height = size
        self.char = char

        self.data = [char * self.width for _ in range(self.height)]

    def clear(self):
        self.data = [self.char * self.width for _ in range(self.height)]

    def add_str(self, pos: Tuple[int, int], string: str):
        x, y = pos

        source_ind = y - 1
        line = self.data[source_ind]

        stard_ind = x - 1
        line_start = line[:stard_ind]

        end_ind = len(string) + x - 1
        line_end = line[end_ind:]

        self.data[source_ind] = line_start + string + line_end
