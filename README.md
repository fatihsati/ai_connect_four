# ai_connect_four
Playing connect four game as AI.

Alpha - Beta pruning is implemented according to the pseudo code on the lecture slides. (ch 6, page: 20)
It works, checks less node with the same efficiency.

## Heuristic 1
Counts the occurances of three blocks for each player.
[1, 1, 1, 2, 1, 2, 1, 2] -> 1 (plyr 1 has 1, plyr 2 has 0) evaulation func: 1

## Heuristic 2
Counts the number of possible "4 in a row" on the board.
[1, 1, 0, 0, 0, 0, 2, 0] -> (plyr 1: 3, plyr 2: 3) evaluation func: 0

## TODO
- [X] game implementation
- [X] ai implementation with basics (utility function)
- [X] h1
- [X] h2
- [ ] h3
- [ ] Update Print board function to look fancy