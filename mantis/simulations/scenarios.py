from mantis.player.player import Player
from mantis.player.style import Style
from mantis.game.game import Game

import copy
import itertools

def run_simulation(players: list[Player], num_times: int) -> dict[int, int]:
    distribution = {}
    for player in players:
        distribution[player.id] = 0

    for _ in range(num_times):
        winning_players = Game(copy.deepcopy(players)).play()
        for winning_player in winning_players:
            distribution[winning_player.id] += 1
    return distribution

def print_result(players: list[Player], distribution: dict[int, int], num_times: int) -> None:
    print(f"\n\nPlayed styles: {", ".join([str(player.id) + ',' + player.style.name for player in players])}")
    for k, v in distribution.items():
        print(f"{k} -> {v} / {num_times} = {"{:.3%}".format( v / num_times)} ")

def run_and_print(players: list[Player], num_times: int) -> None:
    print_result(players, run_simulation(players, num_times), num_times)

def one_of_each():
    players = [
        Player(id=i, style=style) for i, style in enumerate([s for s in Style])
    ]
    run_and_print(players, 2_000)

def all_2_c_combs():
    players = [
        Player(id=i, style=style) for i, style in enumerate([s for s in Style])
    ]
    for comb in itertools.combinations(players, 2):
        run_and_print(comb, 2_000) 

one_of_each()
all_2_c_combs()