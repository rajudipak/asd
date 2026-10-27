def nxt(x, y):
    a, b = 3, 4
    t = min(x, b-y)
    u = min(y, a-x)
    return [(a,y), (x,b), (0,y), (x,0),
            (x-t,y+t), (x+u,y-u)]
 
def dfs(s, vis):
    if s in vis:
        return False
    vis.add(s)
    print("DFS visiting:", s)
    if s[1] == 2:
        print("Goal reached:", s)
        return True
    for n in nxt(*s):
        if n not in vis and dfs(n, vis):
            return True
    return False
 
dfs((0,0), set())