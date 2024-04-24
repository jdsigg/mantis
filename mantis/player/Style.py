from enum import Enum

class Style(Enum):
    """Play styles for non-human players."""
    # Randomly choose every decision. The player will:
    #  - Randomly choose between steal / score.
    #  - When stealing, they'l select a random player to steal from.
    RANDOM = 0
    # No matter what, the player will always choose to score.
    SCORE = 1
    # Calculates the expected value from the options presented to the player.
    VALUE = 2
    # TODO(johnsigg) add more game modes.