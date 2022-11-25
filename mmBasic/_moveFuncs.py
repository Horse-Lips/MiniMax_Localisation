import networkx as nx
from math     import inf
from networkx import shortest_path_length as pathLen
from networkx import single_source_dijkstra_path_length as dijkLen


def getMoves(self, player):
    """
     - Get the move for the current player. For the
     - beacon and target's initial move  this is all 
     - nodes on the graph, for every following target 
     - move it is the target's neighbours.
    """
    if player == 1 or self["pNum"] == 0:
        return [i for i in range(len(self.tree))]

    else:
        return [self["tList"][-1]] + [i for i in self.tree.neighbors(self["tList"][-1])]


def makeMove(self, player, node):
    """
     - Given player and node, make move for player.
    """
    if player == 1:
        self["pNum"] += 1
        self["pList"].append(node)

    else:
        self["tList"].append(node)
        

def undoMove(self, player):
    """
     - "Undoes" the last move made by the player.
    """
    if player == 1:
        self["pNum"]  = self["pNum"] - 1
        self["pList"] = self["pList"][0:-1]

    else:
        self["tList"] = self["tList"][0:-1]


def getTSet(self, tSet, p = None, t = None):
    for i in range(len(self["pList"])):
        if p == None: p = self["pList"][i]    #Get current probe location
        if t == None: t = self["tList"][i]    #Get current target location

        d  = pathLen(self.tree, p, t)    #Dist from probe to target
        ds = dijkLen(self.tree, p)       #Dist from probe to all nodes

        tSet = [i for i in ds if ds[i] == d] if tSet == [] else [i for i in ds if ds[i] == d and i in tSet]

        if len(tSet) == 1:
            return tSet

        neighbSet = []
        for node in tSet:   #Target moves
            neighbSet += [i for i in self.tree.neighbors(node)]

        tSet += neighbSet

        tSet = list(set(tSet))

    return tSet


def expandTSet(self, tSet):
    neighbSet = []

    for node in tSet:
        neighbSet += [i for i in self.tree.neighbors(node)]

    tSet += neighbSet
    return list(set(tSet))
