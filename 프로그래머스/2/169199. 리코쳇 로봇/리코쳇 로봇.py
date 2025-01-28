from collections import deque

def solution(board):
    # 보드 크기
    rows, cols = len(board), len(board[0])
    
    # R(로봇)과 G(목표 지점)의 위치 찾기
    start, goal = None, None
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "R":
                start = (r, c)
            elif board[r][c] == "G":
                goal = (r, c)

    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS를 위한 큐와 방문 기록
    queue = deque([(start[0], start[1], 0)])  # (현재 x, 현재 y, 이동 횟수)
    visited = set()
    visited.add(start)
    
    while queue:
        x, y, moves = queue.popleft()
        
        # 목표 위치에 도달하면 이동 횟수 반환
        if (x, y) == goal:
            return moves
        
        # 4방향으로 이동
        for dx, dy in directions:
            nx, ny = x, y
            
            # 장애물 또는 보드 끝까지 이동
            while 0 <= nx + dx < rows and 0 <= ny + dy < cols and board[nx + dx][ny + dy] != "D":
                nx += dx
                ny += dy
            
            # 이동 후 위치가 방문되지 않았으면 큐에 추가
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, moves + 1))
    
    # 목표 위치에 도달할 수 없으면 -1 반환
    return -1
