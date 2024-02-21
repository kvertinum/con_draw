from con_draw import Manager, Screen, EventTypes


manager = Manager()
screen = Screen()
x = 1


for event in manager.events(0.05):
    if event.type == EventTypes.QUIT:
        manager.quit()
        break

    elif event.type == EventTypes.KEY_PRESS:
        if event.key == "a":
            x -= 1
        elif event.key == "d":
            x += 1

    screen.add_str((x, 1), "#")
    screen.add_str((1, 2), str(manager.last_keys))

    screen.update()
