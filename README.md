<h1 align="center">
  con_draw (0.x)
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/made%20by-Kvertinum01-green">
</p>

> Easy cross-platform framework for drawing in console

## Hello World

```python
from con_draw import Manager, Screen, EventTypes

manager = Manager()
screen = Screen()


for event in manager.events():
    if event.type == EventTypes.QUIT:
        manager.quit()
        break

    screen.add_str((1, 1), "Hello, worl!")
    screen.update()

```

> More examples [here](/examples)

## Installation

### Latest version

```shell
pip install -U "git+https://github.com/Kvertinum01/con_draw"
```
