from abc import ABCMeta, abstractmethod
from typing import Tuple, List

from .list_builder import add_str


class Figure:
    __metaclass__ = ABCMeta

    @abstractmethod
    def _check_cords(self, wh: Tuple[int, int]):
        """raise error on bad cords"""

    @abstractmethod
    def _result_list(self, bg_char: str) -> List[str]:
        """return a ready-made list"""

    @abstractmethod
    def collide_point(self, point: Tuple[int, int]) -> bool:
        """return result of collision with point"""


class FillRect(Figure):
    def __init__(self, pos: Tuple[int, int], wh: Tuple[int, int], char: str):
        self.pos = pos
        self.char = char
        self.width, self.height = wh

    def _check_cords(self, wh: Tuple[int, int]):
        x, y = self.pos
        mz = x < 1 or y < 1
        if x > wh[0] or y > wh[1] or mz:
            raise ValueError(f"Bad x or y ({x};{y})")

    def collide_point(self, point: Tuple[int, int]):
        return False

    def __build_rect(self, bg: List[str]):
        t_bg = bg.copy()

        for ind in range(self.height):
            x, y = self.pos
            t_bg = add_str(t_bg, (x, y + ind), self.char * self.width)

        return t_bg

    def _result_list(self, bg: List[str]):
        return self.__build_rect(bg)


class EmptyRect(Figure):
    def __init__(self, pos: tuple, wh: tuple, char: str, line_size=1):
        self.pos = pos
        self.char = char
        self.line_size = line_size
        self.width, self.height = wh

    def _check_cords(self, wh: Tuple[int, int]):
        x, y = self.pos
        mz = x < 1 or y < 1
        if x > wh[0] or y > wh[1] or mz:
            raise ValueError(f"Bad x or y ({x};{y})")

    def collide_point(self, point: Tuple[int, int]):
        return False

    def __build_rect(self, bg: List[str]):
        t_bg = bg.copy()

        for i in range(self.height):
            t_pos = [self.pos[0], self.pos[1] + i]

            if i <= self.line_size - 1 or i >= self.height - self.line_size:
                t_bg = add_str(t_bg, t_pos, self.char * self.width)
                continue

            for _ in range(2):
                t_bg = add_str(t_bg, t_pos, self.char * self.line_size)
                t_pos[0] += self.width - self.line_size

        return t_bg

    def _result_list(self, bg: List[str]):
        return self.__build_rect(bg)


class Line(Figure):
    def __init__(self, pos1: Tuple[int, int], pos2: Tuple[int, int], char: str):
        self.pos1 = pos1
        self.pos2 = pos2
        self.char = char

    def _check_cords(self, wh: Tuple[int, int]):
        pass

    def collide_point(self, point: Tuple[int, int]):
        return False

    def __build_line(self, bg: List[str]):
        t_bg = bg.copy()

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

        t_bg = add_str(t_bg, (x, y), self.char)

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
            t_bg = add_str(t_bg, (x, y), self.char)

        return t_bg

    def _result_list(self, bg: List[str]):
        return self.__build_line(bg)
