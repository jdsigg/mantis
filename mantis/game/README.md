# Playing Mantis

## Command
(From project root) `$ poetry run python3.12 mantis/game/game.py <players>`

## Command Line Arguments
`game.py` takes in a list of `players` as parameters.

### Players
Players have two types, `human` and `computer`. They are passed into `game.py` as a list. The order in which they are configured represents the order with which players sit next to one another.

#### Humans
Humans are simply represented as `H/h`. If no humans are present, the game is not interactive and will play out silently.
#### Computers
Computers are represented as `[C/c]-<style>`. The computer styles are as such:

- `R/r` (Random): Every decision that can be made is made randomly.
- `S/s` (Score): The player will always try to score.
- `V/v` (Value): The player considers all possible choices and considers the best value play.
- `V+/v+` (Value+): Value mode, but the player only considers the top card's true value.

## Examples

- Three players, the first and second are humans, the last is a random computer
  - `h H c-r`
- Two players, both humans
  - `H h`
- Four computers, two random, followed by two scoring
  - `C-R c-r c-S C-s`
