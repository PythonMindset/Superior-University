import math

def minimax(depth,node_index,is_max,scores,height):
    if depth==height:
        return scores[node_index]
    
    if is_max:
        return max(minimax(depth+1,node_index*2,False,scores,height),
            minimax(depth+1,node_index*2+1,False,scores,height))
    else:
        return min(minimax(depth+1,node_index*2,True,scores,height),
            minimax(depth+1,node_index*2+1,True,scores,height))

scores=[9,4,2,8,1,3,6,8]
height=math.log2(len(scores))
print("The optimal value is:")
print(minimax(0,0,True,scores,height))