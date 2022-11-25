from networkx import shortest_path_length as pathLen
from networkx import single_source_dijkstra_path_length as dijkLen
from math import inf
from ._moveFuncs import getTSet, expandTSet


def tScoreTarget(self, winCond = False, diminish = False):
    """
     - Target-oriented position scoring function. Target scores
     - more if there are more available moves on the next turn.
     - Args:
        - self:     MiniMax object
        - winCond:  True if the win condition should be scored
        - diminish: True if a node's score should be reduced the more it is occupied
    """
    if winCond and self["tWin"] == self["pNum"]:
        return -1 * inf

    tScore = 0

    for t in self["tList"]:
        score = len([i for i in self.tree.neighbors(t)]) + 1 #Score for occupying the node

        if diminish: tScore -= (score * (1 -  (self["tList"].count(t) / len(self["tList"]))))
        else:        tScore -= score

    return tScore


def tScoreProbe(self, winCond = False):
    """
     - Target-oriented position scoring function. Probe scores
     - more if there are less available moves for the target.
     - Args:
        - self:    MiniMax object
        - winCond: True if the win condition should be scored
    """
    tSet = []
    pScore = 0

    for i in range(len(self["pList"])):
        p = self["pList"][i]
        t = self["tList"][i]

        if winCond and t == p:
            return len(self.tree)

        tSet = getTSet(self, tSet, p = p, t = t)
        
        if len(tSet) == 1:
            if winCond:
                return len(self.tree)

            else:
                expandTSet(self, tSet)

        pScore += (len(self.tree) - len(tSet))

    return pScore


def dScoreProbe(self, d, winCond = False, diminish = False):
    """
     - Distance-oriented position scoring function. Probe scores
     - more if successive probes reduce the distance to the target.
     - Args:
        - self:    MiniMax object
        - winCond: True if the win condition should be scored
    """
    pScore = 0

    for i in range(1, len(self["pList"])):
        p0 = self["pList"][i - 1]
        t0 = self["tList"][i - 1]
        p1 = self["pList"][i]
        t1 = self["tList"][i]

        d0 = pathLen(self.tree, p0, t0)
        d1 = pathLen(self.tree, p1, t1)

        if (d1 - d0) >= d :
            if diminish and self["pList"].count(p0) > 3 and self["pList"].count(p1) > 3:
                pScore -= 1

            else:
                pScore += 1

        else:
            pScore -= 1

    return pScore


def dScoreProbeCum(self, winCond = False, diminish = False):
    pScore = 0

    for i in range(len(self["pList"]) - 1):
        p0 = self["pList"][i]
        t0 = self["tList"][i]
        d0 = pathLen(self.tree, p0, t0)

        for j in range(i + 1, len(self["pList"])):
            d1 = pathLen(self.tree, self["pList"][j], self["tList"][j])

            if d1 < d0:
                pScore += 1

            else:
                pScore -= 1

    return pScore

