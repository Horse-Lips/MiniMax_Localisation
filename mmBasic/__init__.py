from math import inf
import networkx as nx
from random import choice
from ._moveFuncs import getMoves, makeMove, undoMove


class Minimax():
    """
     - MiniMax solver class for the localisation game.
     - the solve() function acts as the main method.
     - Target plays as player -1 and the beacon as +1.
     - Variables:
        - tree  - NetworkX tree object
        - iDict - Dict of useful information during execution containing:
            - probeNum  - The number of probes made
            - probeList - List of probed nodes
            - t         - List of nodes target was at 
            - tWin      - The number of probes until the target wins
            - maxDepth  - The maximum number of moves to look ahead
            - win       - ID of winning player
    """
    def __init__(self, tree):
        self.tree  = tree           #nx tree object
        self.iDict = dict()         #Stores useful information during execution

        self.iDict["pNum"]  = 0     #Number of probes
        self.iDict["pList"] = []    #List of probed nodes

        self.iDict["tList"]    = []     #List of target locations
        self.iDict["tWin"] = len(tree)  #Number of probes before target wins


    def __setitem__(self, key, value):
        self.iDict[key] = value


    def __getitem__(self, key):
        try:    return self.iDict[key]
        except: return None


    def minimax(self, depth, player):
        bestMove = [0, -1 * player * inf]  #Best move, -inf for + player, +inf for - player

        if depth == 0:
            return [-1, self["eval"](self, player)]

        for i in getMoves(self, player):
            makeMove(self, player, i)   #Make move for player
            score = self.minimax(depth - 1, -1 * player)   #Analyse move
            undoMove(self, player)                  #"Undo" move

            score[0] = i            #The actual move to play

            if (player == 1 and score[1] > bestMove[1]) or (player == -1 and score[1] < bestMove[1]):
                bestMove = score        #If score exceeds current best then play move

        return bestMove #Return best move found

