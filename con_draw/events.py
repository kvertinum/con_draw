from enum import Enum


class EventTypes(Enum):
    KEY_PRESS = "key_press"


class Event:
    key: str

    def __init__(self, type: str, **kwargs):
        self.type = type

        for k, v in kwargs.items():
            setattr(self, k, v)
