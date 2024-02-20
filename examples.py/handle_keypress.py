from con_draw import Drawer


drawer = Drawer()
x = 1


for frame in drawer.frames():
    if frame.key == "a":
        x -= 1
    elif frame.key == "d":
        x += 1

    frame.add_str((x, 1), "#")
    frame.add_str((1, 2), str(drawer.last_keys))

    frame.update()
