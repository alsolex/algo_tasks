class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        G = self.buildGraph(grid)
        # visited = np.zeros(len(G)).astype(bool)
        return self.BFS(G, 0)

    def buildGraph(self, grid):
        n, m = len(grid), len(grid[0])
        vertexes = list(range(n * m))
        edges = []

        for i in range(n):
            for j in range(m):
                edges.append([])
                if grid[i][j] == 1:
                    continue
                v_idx = i * n + j

                if i > 0 and j > 0:
                    if grid[i - 1][j - 1] == 0:
                        edges[-1].append(v_idx - m - 1)
                if i > 0:
                    if grid[i - 1][j] == 0:
                        edges[-1].append(v_idx - m)
                if i > 0 and j + 1 < m:
                    if grid[i - 1][j + 1] == 0:
                        edges[-1].append(v_idx - m + 1)
                if j > 0:
                    if grid[i][j - 1] == 0:
                        edges[-1].append(v_idx - 1)
                if j + 1 < m:
                    if grid[i][j + 1] == 0:
                        edges[-1].append(v_idx + 1)
                if i + 1 < n and j > 0:
                    if grid[i + 1][j - 1] == 0:
                        edges[-1].append(v_idx + m - 1)
                if i + 1 < n:
                    if grid[i + 1][j] == 0:
                        edges[-1].append(v_idx + m)
                if i + 1 < n and j + 1 < m:
                    if grid[i + 1][j + 1] == 0:
                        edges[-1].append(v_idx + m + 1)
        return edges

    def DFS(self, G, visited, vertex, distance):
        if vertex == len(G) - 1:
            return distance
        visited[vertex] = True
        for neighbor in G[vertex]:
            if not visited[neighbor]:
                return self.DFS(G, visited, neighbor, distance + 1)
        return -1

    def BFS(self, G, vertex):
        queue = deque()
        marked = set()
        marked.add(vertex)
        queue.append((vertex, 0))

        depth = 0
        while queue:
            r, d = queue.popleft()
            if r == len(G) - 1:
                return d + 1
            if d > depth:
                depth += 1
            for node in G[r]:
                if node not in marked:
                    marked.add(node)
                    queue.append((node, depth + 1))
        return -1
