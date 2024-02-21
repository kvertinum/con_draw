import os
import time
from typing import Any

from .kbhit import KBHit
from .events import EventTypes, EventManager


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


class Manager:
    def __init__(self, key_queue_size=3):
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

    def events(self, delay=0.4, no_delay=False):
        events = EventManager()

        while self.__loop:
            try:
                if self.keyboard.kbhit():
                    key = self.keyboard.getch()

                    events.reg_event(EventTypes.KEY_PRESS, key=key)
                    self._last_keys.append(key)

                tm_pause = time.time() - self.__last_time >= delay

                if tm_pause or no_delay:
                    events.reg_event(EventTypes.NEW_FRAME)

                    for event in events.gen():
                        yield event

                    events.clear()

                    self.__last_time = time.time()

            except KeyboardInterrupt:
                events.reg_event(EventTypes.QUIT)
