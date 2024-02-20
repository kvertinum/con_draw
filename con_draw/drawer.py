import os
import time
from typing import Any, List

from .frame import Frame
from .kbhit import KBHit
from .events import Event, EventTypes


class LastKeys:
    def __init__(self, size: int):
        self.size = size
        self.m = []

    @property
    def last_element(self):
        if len(self.m) != 0:
            return self.m[-1]
        return None

    def append(self, data: Any):
        if data == self.last_element or not data:
            return
        sr = 1 if len(self.m) == self.size else 0
        self.m = self.m[sr:] + [data]


class Drawer:
    def __init__(self, bg_char=" ", key_queue_size=3):
        self.bg_char = bg_char
        self.keyboard = KBHit()

        self._last_keys = LastKeys(key_queue_size)

        self.__loop = True
        self.__last_time = 0

        os.system("cls || clear")

    @property
    def last_keys(self):
        return self._last_keys.m

    def quit(self):
        self.__loop = False

    def frames(self, pause=0.4):
        events: List[Event] = []

        while self.__loop:
            if self.keyboard.kbhit():
                key = self.keyboard.getch()

                event = Event(EventTypes.KEY_PRESS, key=key)
                self._last_keys.append(key)

                events.append(event)

            tm_pause = time.time() - self.__last_time >= pause

            if tm_pause:
                frame = Frame(self.bg_char, events)

                yield frame
                events = []

                self.__last_time = time.time()
