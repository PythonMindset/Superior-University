import math
# cd= currnt depth
# nd= node index
# mt= max turn
# sc= scores
# td= target depth
def minimax (cd, ni, mt, sc, td):
    if (cd==td):
        return sc[ni]

    if (mt):
        return max(minimax(cd + 1, ni * 2, False, sc, td),
        minimax(cd + 1, ni * 2 + 1, False, sc, td))
    else:
        return min(minimax(cd + 1, ni * 2, True, sc, td),
        minimax(cd + 1, ni * 2 + 1, True, sc, td))

scores=[3, 5, 2, 9, 3, 5, 2, 9]
treeDepth=int(math.log(len(scores), 2))
print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores, treeDepth))