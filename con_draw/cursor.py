import os

if os.name == "nt":
    import ctypes
    from ctypes import c_long, c_ulong

    g_handle = ctypes.windll.kernel32.GetStdHandle(c_long(-11))

    def move_cursor(x: int, y: int):
        value = x + (y << 16)
        ctypes.windll.kernel32.SetConsoleCursorPosition(g_handle, c_ulong(value))

else:

    def move_cursor(x: int, y: int):
        pass
