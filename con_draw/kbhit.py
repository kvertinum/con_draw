import os

if os.name == "nt":
    import msvcrt

else:
    import sys
    import termios
    import atexit
    from select import select


class KBHit:
    def __init__(self):
        if os.name != "nt":
            self.fd = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.fd)
            self.old_term = termios.tcgetattr(self.fd)

            self.new_term[3] = self.new_term[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)

            atexit.register(self.set_normal_term)

    def set_normal_term(self):
        if os.name != "nt":
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)

    def getch(self):
        if os.name == "nt":
            bytes_string = b""
            while self.kbhit():
                bytes_string += msvcrt.getch()

        else:
            bytes_string = sys.stdin.buffer.read1()

        return self.decode_bytes(bytes_string)

    def decode_bytes(self, bytes_string: bytes):
        base_replaces = {"\x1b": "ESCAPE", "\r": "\n", "\x08": "BACKSPACE"}

        first = bytes_string[0]
        if len(bytes_string) == 1:
            decoded = chr(first)
            return base_replaces.get(decoded) or decoded

        if os.name == "nt":
            mv = 0

            letters_dict = {
                "K": "ARROW_LEFT",
                "H": "ARROW_UP",
                "M": "ARROW_RIGHT",
                "P": "ARROW_DOWN",
            }

        else:
            mv = 1

            letters_dict = {
                "D": "ARROW_LEFT",
                "A": "ARROW_UP",
                "C": "ARROW_RIGHT",
                "B": "ARROW_DOWN",
            }

        decoded_bytes = bytes_string.decode("utf-8", "ignore")

        if len(bytes_string) == mv + 2:
            key_letter = chr(bytes_string[mv + 1])
            return letters_dict.get(key_letter) or decoded_bytes

        return decoded_bytes

    def kbhit(self):
        if os.name == "nt":
            return msvcrt.kbhit()

        else:
            dr, _, _ = select([sys.stdin], [], [], 0)
            return dr != []
