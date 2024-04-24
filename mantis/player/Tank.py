from mantis.deck.card import Card
from mantis.deck.color import Color
import random

class Tank:
    def __init__(self):
        self.cards: list[Card] = []

    def add(self, card: Card) -> None:
        """Adds a card to the tank."""
        self.cards.append(card)

    def size(self) -> int:
        return len(self.cards)

    def take(self, color: Color) -> list[Card]:
        """Remove all cards of a certain color from the tank."""
        to_take = [card for card in self.cards if card.color == color]
        self.cards = [card for card in self.cards if card.color != color]
        return to_take

    def __str__(self):
        colors_to_counts: dict[Color, int] = {}
        for card in self.cards:
            if card.color in colors_to_counts:
                colors_to_counts[card.color] += 1
            else:
                colors_to_counts[card.color] = 1
        return ", ".join([f"{count} {str(color)}" for color, count in colors_to_counts.items()])
    
# For sanity testing.
if __name__ == "__main__":
    tank = Tank()
    colors = [color for color in Color]
    for color in colors:
        tank.add(Card(color, list()))

    # Add some random cards to the tank.
    for _ in range(10):
        tank.add(Card(random.choice(colors), list()))
    
    # Remove some random colors from the tank.
    for _ in range(4):
        print(tank.take(random.choice(colors)))

    print()
    print(tank)
    print()