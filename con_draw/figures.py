from abc import ABCMeta, abstractmethod
from typing import Tuple, List

from .canvas import Canvas


class Figure:
    __metaclass__ = ABCMeta

    @abstractmethod
    def _result_list(self, canvas: Canvas) -> List[str]:
        """return a ready-made list"""

    @abstractmethod
    def collide_point(self, point: Tuple[int, int]) -> bool:
        """return result of collision with point"""


class FillRect(Figure):
    def __init__(self, pos: Tuple[int, int], wh: Tuple[int, int], char: str):
        self.pos = pos
        self.char = char
        self.width, self.height = wh

    def collide_point(self, point: Tuple[int, int]):
        return False

    def __build_rect(self, canvas: Canvas):
        for ind in range(self.height):
            x, y = self.pos
            canvas.add_str((x, y + ind), self.char * self.width)

    def _result_list(self, canvas: Canvas):
        self.__build_rect(canvas)


class EmptyRect(Figure):
    def __init__(self, pos: tuple, wh: tuple, char: str, line_size=1):
        self.pos = pos
        self.char = char
        self.line_size = line_size
        self.width, self.height = wh

    def collide_point(self, point: Tuple[int, int]):
        return False

    def __build_rect(self, canvas: Canvas):
        for i in range(self.height):
            t_pos = [self.pos[0], self.pos[1] + i]

            if i <= self.line_size - 1 or i >= self.height - self.line_size:
                canvas.add_str(t_pos, self.char * self.width)
                continue

            for _ in range(2):
                canvas.add_str(t_pos, self.char * self.line_size)
                t_pos[0] += self.width - self.line_size

    def _result_list(self, canvas: Canvas):
        self.__build_rect(canvas)


class Line(Figure):
    def __init__(self, pos1: Tuple[int, int], pos2: Tuple[int, int], char: str):
        self.pos1 = pos1
        self.pos2 = pos2
        self.char = char

    def collide_point(self, point: Tuple[int, int]):
        return False

    def __build_line(self, canvas: Canvas):
        x1, y1 = self.pos1
        x2, y2 = self.pos2

        dx = x2 - x1
        dy = y2 - y1

        sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
        sign_y = 1 if dy > 0 else -1 if dy < 0 else 0

        if dx < 0:
            dx = -dx
        if dy < 0:
            dy = -dy

        if dx > dy:
            pdx, pdy = sign_x, 0
            es, el = dy, dx
        else:
            pdx, pdy = 0, sign_y
            es, el = dx, dy

        x, y = x1, y1

        error, t = el / 2, 0

        canvas.add_str((x, y), self.char)

        while t < el:
            error -= es
            if error < 0:
                error += el
                x += sign_x
                y += sign_y
            else:
                x += pdx
                y += pdy
            t += 1
            canvas.add_str((x, y), self.char)

    def _result_list(self, canvas: Canvas):
        self.__build_line(canvas)
