from dataclasses import dataclass
from mantis.deck.color import Color

@dataclass
class Card():
    color: Color
    back: list[Color]