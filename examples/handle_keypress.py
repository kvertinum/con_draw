from con_draw import Drawer
from con_draw.events import EventTypes


drawer = Drawer()
x = 1


for frame in drawer.frames():
    for event in frame.events:
        if event.type == EventTypes.KEY_PRESS:
            if event.key == "a":
                x -= 1
            elif event.key == "d":
                x += 1

    frame.add_str((x, 1), "#")
    frame.add_str((1, 2), str(drawer.last_keys))

    frame.update()
