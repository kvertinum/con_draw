from con_draw import Screen, Manager, EventTypes
from con_draw.figures import FillRect, Line


manager = Manager()
screen = Screen()

base_rect = FillRect((1, 1), (5, 5), "#")
base_line = Line((7, 1), (11, 5), "#")


for event in manager.events(0.05):
    if event.type == EventTypes.QUIT:
        manager.quit()
        break

    screen.add_figure(base_rect)
    screen.add_figure(base_line)

    screen.update()
