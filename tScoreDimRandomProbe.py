from mmBasic            import Minimax
from mmBasic._moveFuncs import makeMove, getTSet
from mmBasic._evalFuncs import tScoreTarget, tScoreProbe
from random             import choice
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import trees


def eval(self, player):
    if   player == -1: return tScoreTarget(self, diminish = True)
    elif player == 1:  return tScoreProbe(self)

np.random.seed(5)
useGraph = trees.er

solver = Minimax(useGraph)
solver["depth"] = 4
solver["eval"]  = eval

tSet   = []

while solver["win"] is None:
    tMove = solver.minimax(solver["depth"], -1)
    print("=== Player:", -1, " ===")
    print("- Move:", tMove[0])
    print("- Score:", tMove[1])

    makeMove(solver, -1, tMove[0])

    pMove = choice(range(len(useGraph)))
    print("=== Player: 1 ===")
    print("- Move:", pMove)

    makeMove(solver, 1, pMove)

    if   solver["tWin"] == solver["pNum"]:
        solver["win"] = -1

    elif solver["pNum"] > 0:
        if solver["pList"][-1] == solver["tList"][-1]:
            solver["win"] = 1

        elif len(getTSet(solver, tSet)) == 1:
            solver["win"] = 1

print("Winner:", solver["win"])
print("Probe locations:", solver["pList"])
print("Target locations:", solver["tList"])

nx.draw(useGraph, with_labels = True)
plt.show()
