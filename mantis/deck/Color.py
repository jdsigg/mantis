from enum import Enum

class Color(Enum):
    # Hand-picked ANSI color codes. Reference: https://talyian.github.io/ansicolors/
    RED = '38;5;196'
    GREEN = '38;5;47'
    YELLOW = '38;5;226'
    BLUE = '38;5;39'
    PURPLE = '38;5;92'
    PINK = '38;5;201'
    ORANGE = '38;5;214'

    def __str__(self):
        return '\x1b[' + self.value + 'm' + self.name[0] + self.name[1:].lower() + '\x1b[0m'
    
    def __repr__(self):
        return self.__str__()
    
# For sanity testing.
if __name__ == "__main__":
    print(Color.RED)
    print(Color.GREEN)
    print(Color.YELLOW)
    print(Color.BLUE)
    print(Color.PURPLE)
    print(Color.PINK)
    print(Color.ORANGE)