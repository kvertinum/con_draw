import sys
import os
from typing import List, Tuple

from .figures import Figure
from .canvas import Canvas
from .events import Event


class Frame:
    def __init__(self, bg_char: str, events: List[Event]):
        self.win_size = os.get_terminal_size()
        self.width, self.height = self.win_size
        self.events = events

        self._canvas = Canvas(self.win_size, bg_char)

    def _check_pos(self, pos: Tuple[int]):
        x, y = pos
        mz = x < 1 or y < 1
        if x > self.width or y > self.height or mz:
            raise ValueError(f"Bad x or y ({x};{y})")

    def add_str(self, pos: Tuple[int], string: str):
        self._check_pos(pos)

        self._canvas.add_str(pos, string)

    def add_list(self, pos: Tuple[int], strings: List[str]):
        self._check_pos(pos)

        for ind, string in enumerate(strings):
            self.add_str((pos[0], pos[1] + ind), string)

    def add_figure(self, figure: Figure):
        figure._result_list(self._canvas)

    def update(self):
        print("\033[H\033[3J", end="")

        str_result = "\n".join(self._canvas.data)
        sys.stdout.write(str_result)
