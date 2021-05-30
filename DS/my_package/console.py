import sys

class _console:
    END= '\x1b[0m'

    def get_style(fg,bg):
        format = ';'.join([str(7), str(fg), str(bg)])
        return "\x1b["+format+"m"

    RED=get_style(31,47)
    GREEN=get_style(30,42)
    YELLOW=get_style(33,47)
    BLUE=get_style(34,47)

    @staticmethod
    def log(msg):
        print(msg)

    @staticmethod
    def style_msg(msg,color):
        if "linux" not in sys.platform.lower():
            return msg
        return "{}{}{}".format(color,msg,_console.END)

    @staticmethod
    def error(msg):
        msg=str(msg)
        for line in msg.split("\n"):
            print(_console.style_msg(line,_console.RED),file=sys.stderr)

    @staticmethod
    def info(msg):
        msg=str(msg)
        for line in msg.split("\n"):
            print(_console.style_msg(line,_console.GREEN))

    @staticmethod
    def warning(msg):
        msg=str(msg)
        for line in msg.split("\n"):
            print(_console.style_msg(line,_console.YELLOW))

    @staticmethod
    def debug(msg):
        msg=str(msg)
        for line in msg.split("\n"):
            print(_console.style_msg(line,_console.BLUE))

