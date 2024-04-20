from dataclasses import dataclass
from mantis.deck.Color import Color

@dataclass
class Card():
    color: Color
    back: list[Color]