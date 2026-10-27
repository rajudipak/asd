from queue import PriorityQueue
 
def h(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
 
def astar(grid, start, goal):
    q = PriorityQueue()
    q.put((h(start, goal), start))
    parent, cost = {}, {start: 0}
    while not q.empty():
        _, cur = q.get()
        if cur == goal:
            path = []
            while cur in parent:
                path.append(cur)
                cur = parent[cur]
            return [start] + path[::-1]
        x, y = cur
        for a, b in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0 <= a < len(grid) and 0 <= b < len(grid[0]) and grid[a][b] == 0:
                nxt = (a,b)
                g = cost[cur] + 1
                if nxt not in cost or g < cost[nxt]:
                    cost[nxt] = g
                    parent[nxt] = cur
                    q.put((g + h(nxt, goal), nxt))
    return None
 
grid = [
    [0,0,0,0,0],
    [0,1,1,0,0],
    [0,0,0,1,0],
    [0,1,0,0,0],
    [0,0,0,1,0]
]
print("Path Found:")
print(astar(grid, (0,0), (4,4)))