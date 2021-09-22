from enum import Enum,auto

class Color(Enum):
    RED=auto()
    BLUE="BLUEEEE"
    GREEN=auto()

# print(hasattr(Color,"RED"))
# print(Color.RED.value)

print(Color['REDs'])