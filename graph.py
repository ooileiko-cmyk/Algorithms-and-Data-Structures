import heapq

# -----------------------------
# 1. Матрица смежности (взвешенный направленный граф)
# -----------------------------
graph_matrix = [
    [0, 4, 2, 0, 0],
    [0, 0, 5, 10, 0],
    [0, 0, 0, 3, 0],
    [0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0]
]

n = len(graph_matrix)

# -----------------------------
# 2. Перевод в список смежности
# -----------------------------
graph = {i: [] for i in range(n)}

for i in range(n):
    for j in range(n):
        if graph_matrix[i][j] != 0:
            graph[i].append((j, graph_matrix[i][j]))

print("СПИСОК СМЕЖНОСТИ:")
for k, v in graph.items():
    print(k, "->", v)

# -----------------------------
# 3. BFS (обхід в ширину)
# -----------------------------
def bfs(start):
    visited = [False] * n
    queue = [start]
    visited[start] = True

    print("\nBFS:")
    while queue:
        v = queue.pop(0)
        print(v, end=" ")

        for to, w in graph[v]:
            if not visited[to]:
                visited[to] = True
                queue.append(to)

bfs(0)

# -----------------------------
# 4. DFS (обхід в глибину)
# -----------------------------
def dfs(v, visited):
    visited[v] = True
    print(v, end=" ")

    for to, w in graph[v]:
        if not visited[to]:
            dfs(to, visited)

print("\nDFS:")
visited = [False] * n
dfs(0, visited)

# -----------------------------
# 5. Алгоритм Дейкстри
# -----------------------------
def dijkstra(start):
    dist = [float('inf')] * n
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        d, v = heapq.heappop(pq)

        if d > dist[v]:
            continue

        for to, w in graph[v]:
            if dist[to] > dist[v] + w:
                dist[to] = dist[v] + w
                heapq.heappush(pq, (dist[to], to))

    return dist

print("\n\nДейкстра (від вершини 0):")
print(dijkstra(0))