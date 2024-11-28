from collections import deque, defaultdict
import sys

input = sys.stdin.readline

# 1. 입력 받기
N, M, K, X = map(int, input().split())  # 도시 개수, 도로 개수, 거리 K, 시작 도시 X
graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)  # 단방향 도로 저장

# 2. BFS를 이용한 최단 거리 계산
def bfs(start):
    distance = [-1] * (N + 1)  # 모든 도시의 거리 초기화 (-1: 도달 불가능)
    distance[start] = 0  # 시작 도시의 거리는 0
    queue = deque([start])  # BFS를 위한 큐 초기화

    while queue:
        current = queue.popleft()

        # 현재 도시의 거리 제한
        if distance[current] >= K:
            continue

        # 현재 도시에서 이동할 수 있는 모든 도시 탐색
        for next_city in graph[current]:
            if distance[next_city] == -1:  # 아직 방문하지 않은 도시
                distance[next_city] = distance[current] + 1
                queue.append(next_city)

    return distance

# 3. 거리 계산 및 결과 출력
distances = bfs(X)  # 시작 도시 X에서 각 도시까지의 최단 거리 계산
result = [i for i in range(1, N + 1) if distances[i] == K]  # 거리 K인 도시 찾기

# 출력
if result:
    print('\n'.join(map(str, result)))  # 거리 K인 도시 번호를 오름차순 출력
else:
    print(-1)  # 없으면 -1 출력