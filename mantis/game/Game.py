from mantis.deck.Card import Card
from mantis.deck.Color import Color
from mantis.player.Player import Player
from mantis.player.Style import Style
import itertools
import random

class Game():

    def __init__(self, num_players: int, humans: list[int] = [0]):
        # Create the players.
        if num_players < 2 or num_players > 6:
            raise Exception("You must have between 2 and 6 players.")
        
        self.players: list[Player] = []
        for i in range(num_players):
            self.players.append(Player(id=i))
        
        # Place the humans where they'd like to sit.
        for human in humans:
            self.players[human].is_computer = False

        # Keep track of the current player.
        self.player_index = random.choice(range(len(self.players)))

        # Make and shuffle the deck.
        self.deck = []
        colors = [c for c in Color]
        for combination in itertools.combinations(colors, 3):
            colors = list(combination)
            self.deck.append(Card(colors[0], colors))
            self.deck.append(Card(colors[1], colors))
            self.deck.append(Card(colors[2], colors))
        random.shuffle(self.deck)

        # Deal 4 cards to each player.
        for player in self.players:
            for _ in range(4):
                player.give_card(self.deck.pop())

    def clear_screen(self):
        # https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console#answer-50560686
        # Clear the screen.
        print("\033[H\033[2J", end="")

    def get_input(self, prompt: str, *allowed_responses) -> str:
        allowed = set(allowed_responses)
        while True:
            choice = input(prompt).strip()
            if choice in allowed:
                return choice

    def print_start_of_round(self, players: list[Player], player_index: int) -> None:
        self.clear_screen()
        # Print the state of the game.
        for i in range(len(players)):
            print(f"{' * ' if i == player_index else '   '}({i}): {players[i]}")
        print("\n\n")

    def score(self, players: list[Player], player_index: int, card: Card):
        print(f"  Player {player_index} chooses to score.")
        print(f"  The card's color is {card.color}.")
        input("\n  Press Enter to continue...")
        players[player_index].score(card)

    def steal(self, players: list[Player], stealer: int, stealee: int, card: Card):
        print(f"  Player {stealer} chooses to steal from Player {stealee}.")
        print(f"  The card's color is {card.color}.")
        input("\n  Press Enter to continue...")
        taken_cards = players[stealee].take_color(card.color)
        if taken_cards:
            # Give the cards to you if the steal-ee has them.
            players[stealer].give_card(card)
            for taken_card in taken_cards:
                players[stealer].give_card(taken_card)
            # If there are only two players in the game, the stealer goes again.
            if (len(players) == 2):
                self.player_index -= 1
            return True
        
        # Otherwise, give the card to the player.
        players[stealee].give_card(card)
        return False

    def get_other_players(self, players: list[Player], player_index: int) -> list[int]:
        return [i for i in range(len(players)) if i != player_index]

    def make_random_play(self, players: list[Player], player_index: int, card: Card):
        # Randomly select between steal / score.
        choice = round(random.random())
        if choice == 1:
            # 1 is steal.
            self.steal(players, player_index, random.choice(self.get_other_players(players, player_index)), card)
            return
        # 0 is score.
        self.score(players, player_index, card)

    def make_computer_play(self, players: list[Player], player_index: int, card: Card):
        # TODO(johnsigg): Implement more computer play styles.
        player = players[player_index]
        if player.style == Style.RANDOM:
            self.make_random_play(players, player_index, card)
        elif player.style == Style.SCORE:
            self.score(players, player_index, card)

    def get_winners(self, players: list[Player], deck: list[Card]) -> list[Player]:
        winning_score = 15 if len(players) == 2 else 10
        # If any player has `winning_score` or more points, the game is over and that player is the winner.
        players_with_enough_points = [player for player in players if player.points >= winning_score]
        if players_with_enough_points:
            return players_with_enough_points
        
        # If the deck is empty, whoever has the most points wins.
        # If there are multiple players with the same number of points, whoever has the largest tank wins.
        # (Not in the rules) if possible, same size tanks tie and both players win.
        if not deck:
            highest_score = max([player.points for player in players])
            high_scoring_players = [player for player in players if player.points == highest_score]
            if len(high_scoring_players) == 1:
                return high_scoring_players
            # If multiple players have the same score, whoever has the larger tank wins.
            largest_tank = max([player.tank.size() for player in high_scoring_players])
            return [player for player in high_scoring_players if player.tank.size() == largest_tank]

        # Otherwise, the game continues.
        return []

    def play(self):
        # Game loop.
        while True:
            self.player_index = (self.player_index + 1) % len(self.players)
            self.print_start_of_round(self.players, self.player_index)
            
            # See if the game is over and exit accordingly.
            winners = self.get_winners(self.players, self.deck)
            if winners:
                input(f" Players ({",".join([player.id for player in winners])}) win!")
                break

            # The top card is always (1) scored or (2) stolen each round.
            top_card: Card = self.deck.pop()
            print(f"Cards left: {len(self.deck)}, The deck shows: {top_card.back}")
            if self.players[self.player_index].is_computer:
                self.make_computer_play(self.players, self.player_index, top_card)
                continue

            # Player logic.
            choice = self.get_input("  Do you want to score, or steal? ", "score", "steal")
            if choice == "score":
                # Draw from the deck and score.
                self.score(self.players, self.player_index, top_card)
            else:
                # Steal from another player. Map to strings for input matching.
                options = list(map(str, self.get_other_players(self.players, self.player_index)))
                who = int(self.get_input(f"  Who do you want to steal from? ({', '.join(options)}) ", *options))
                self.steal(self.players, self.player_index, who, top_card)

if __name__ == "__main__":
    # TODO(johnsigg): Take in number of players as an argument on the command line.
    Game(5).play()