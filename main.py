import sys

from modes import shellMode, interactiveMode

if len(sys.argv) > 1:
    shellMode()
else:
    interactiveMode()
    