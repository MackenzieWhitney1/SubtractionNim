# SubtractionNim
Read "theory" for general problem statement and example.
This is meant to be a utility to solve the nim game by printing optimal play.

Most direct user functions are show_stat_block and show_optimal_play

show_stat_block gives a word based explanation on what the most rational move is from a given position

show_optimal_play shows the entire chain of moves when the game is played optimally. 

Here is an example of untracked file "TestSpace.py"

import PNLogic

P_List = PNLogic.init(100)

PNLogic.show_optimal_play(P_List, (52, 15))
