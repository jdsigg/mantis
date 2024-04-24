from mantis.deck.card import Card
from mantis.player.tank import Tank
from mantis.player.style import Style

class Player():
    def __init__(self, id: int, is_computer: bool = True, style = Style.RANDOM):
        self.tank = Tank()
        self.points = 0
        self.id = id
        self.is_computer = is_computer
        self.style = style

    def give_card(self, card: Card):
        self.tank.add(card)

    def take_color(self, card: Card):
        return self.tank.take(card)

    def score(self, card: Card):
        # Remove all cards from the tank that match the cards color.
        cards = self.take_color(card.color)
        # If there are any, we score them and the card.
        if cards:
            self.points += len(cards) + 1
            return
        # If there aren't any, keep the card.
        self.tank.add(card)

    def __str__(self):
        return f"Score: {self.points}, Cards: {str(self.tank)}"
    
    def __repr__(self):
        return str(self)