from collections import deque

def solution(maps):

    row = len(maps)
    col = len(maps[0])
    visited = [[False]*col for _ in range(row)]
#    print(visited)
    
    def bfs(x,y):

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        visited[x][y] = True
        
        queue = deque()
        queue.append((x,y,1))
        
        while queue:
            cur_x, cur_y, length = queue.popleft()
            if cur_x == row - 1 and cur_y == col - 1:
                return length
            
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                
                if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
                    if maps[next_x][next_y] == 1 and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y, length+1))
                        
        return -1                
                
    return bfs(0, 0)