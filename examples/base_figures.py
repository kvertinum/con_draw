from con_draw import Drawer
from con_draw.figure import FillRect, Line


drawer = Drawer()

base_rect = FillRect((1, 1), (5, 5), "#")
base_line = Line((7, 1), (11, 5), "#")


for frame in drawer.frames():
    frame.add_figure(base_rect)
    frame.add_figure(base_line)

    frame.update()
