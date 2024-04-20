# mantis
An implementation of the card game, [Mantis](https://www.explodingkittens.com/products/mantis), created by Exploding Kittens.

## Goal
Win the game by:
- Scoring 10 points before any of your opponents
- Having the most points when the deck runs out of cards
  - `TODO(johnsigg) update the tie scenarios`

## Constraints
- A deck of 105 unique cards
- Cards are made up of two parts
  - A colored face
  - A tri-colored back
- There are 7 card colors:
  - ${\textsf{\color{red}Red\color{white}, \color{green}Green\color{white}, \color{Blue}Blue\color{white}, \color{purple}Purple\color{white}, \color{pink}Pink\color{white}, \color{yellow}Yellow\color{white}, and \color{orange}Orange}}$
- There are 15 of each color in the deck
- There are ${7 \choose 3} = 35$ ways to choose 3 colors from 7
- The deck is made by
  - Creating a card for each color in each combination
    - The colored face is the `i`th color in the combination
    - The tri-colored back is the combination itself
- The game is designed for 2-6 players

## How to Play
- 4 cards are dealt face up to each player and placed in their `tank`
- A random player is selected to go first
- Each turn, a player can either `score` or `steal` after inspecting the tri-colored back of the deck's top card
- After `scoring` or `stealing`, the turn is passed to the next player

### Scoring
- The player draws the deck's top card and looks at the face
  - If the card matches a color in their `tank`, the player removes all matching cards in their `tank` and `scores` 1 point for each matching card
  - If the card does not match a color in their `tank`, the player places the card face up in their `tank`

### Stealing
- The player selects a player (that is not them) to steal from
- The player draws the deck's top card and looks at the face
  - If the card matches a color in the stealee's `tank`, the player moves all matching cards from the stealee's `tank` into their `tank`
  - The player does <b>not</b> `score` these cards
 
## Two Player Caveats
- The game goes until 15 points instead of 10
- Successfully `stealing` causes you to take another turn
