from enum import Enum
from typing import List


class EventTypes(Enum):
    NEW_FRAME = 0
    KEY_PRESS = 1
    QUIT = 2


class Event:
    key: str

    def __init__(self, type: int, **kwargs):
        self.type = type

        for k, v in kwargs.items():
            setattr(self, k, v)


class EventManager:
    def __init__(self):
        self.events: List[Event] = []

    def gen(self):
        for event in self.events:
            yield event

    def reg_event(self, type: int, **kwargs):
        event = Event(type, **kwargs)
        self.events.append(event)

    def clear(self):
        self.events = []
