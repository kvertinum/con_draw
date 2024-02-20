<h1 align="center">
  con_draw (0.x)
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/made%20by-Kvertinum01-green">
</p>

> Простейший фреймворк для рисования в консоли

## Hello World

```python
from con_draw import Drawer

drawer = Drawer()

for frame in drawer.frames():
    frame.add_str((3, 5), "Hello world")
    frame.update()
```

> Больше примеров [здесь](/examples)

## Установка

### Новейшая версия

```shell
pip install -U "git+https://github.com/Kvertinum01/con_draw#egg=con_draw"
```