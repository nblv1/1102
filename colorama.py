import sys
from colorama import init, AnsiToWin32
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream


# Python 3
print(Fore.BLUE + 'blue text on stderr', file=stream)