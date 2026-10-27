from collections import deque
 
def nxt(x, y):
    a, b = 3, 4
    t = min(x, b-y)
    u = min(y, a-x)
    return [(a,y), (x,b), (0,y), (x,0),
            (x-t,y+t), (x+u,y-u)]
 
def bfs():
    q = deque([(0,0)])
    vis = set()
    while q:
        s = q.popleft()
        if s in vis:
            continue
        vis.add(s)
        print("BFS visiting:", s)
        if s[1] == 2:
            print("Goal reached:", s)
            return
        q.extend(n for n in nxt(*s) if n not in vis)
 
bfs()