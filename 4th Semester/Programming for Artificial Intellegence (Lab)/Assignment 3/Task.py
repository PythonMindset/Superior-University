def water_jug_dfs(x,y,visited,path):
    if x==2 or y==2:
        print("Goal reached")
        print("Path:")
        for i in path+[(x,y)]:
            print(i)
        return True
    
    visited.add((x,y))
    moves=[]
    moves.append((3,y)) # Fill x
    moves.append((x,4)) # Fill y
    moves.append((0,y)) # Empty x
    moves.append((x,0)) # Empty y
    if x+y<=4: # Pour x in y
        moves.append((0,x+y))
    else:
        moves.append((x-(4-y),4))
    if x+y<=3: # Pour y in x
        moves.append((x+y,0))
    else:
        moves.append((3,y-(3-x)))

    for move in moves:
        if move not in visited:
            if water_jug_dfs(move[0],move[1],visited,path+[(x,y)]):
                return True
    return False

visited=set()
water_jug_dfs(0, 0, visited, [])