import sys

input = sys.stdin.read

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global count
    visited[x][y] = True
    count += 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == 1:
            dfs(nx, ny)
            
data = input().strip().split('\n')
N = int(data[0])
grid = [list(map(int, data[i+1])) for i in range(N)]

visited = [[False]*N for _ in range(N)]
complexes = []

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visited[i][j]:
            count = 0
            dfs(i, j)
            complexes.append(count)
            
complexes.sort()
print(len(complexes))
for c in complexes:
    print(c)