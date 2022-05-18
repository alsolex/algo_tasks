import numpy as np


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:

        G, crit_cons = [[] for _ in range(n)], []
        lowestRank, visited = np.zeros(n), np.zeros(n).astype(bool)

        for connection in connections:
            G[connection[0]].append(connection[1])
            G[connection[1]].append(connection[0])

        self.DFS(crit_cons, G, lowestRank, visited, 0, -1, 0)
        return crit_cons

    def DFS(self, crit_cons, G, lowestRank, visited, cur_rank, u, v):

        visited[v], lowestRank[v] = True, cur_rank

        for w in G[v]:
            if w == u:
                continue

            if not visited[w]:
                self.DFS(crit_cons, G, lowestRank, visited, cur_rank + 1, v, w)

            lowestRank[v] = min(lowestRank[v], lowestRank[w])
            if lowestRank[w] == cur_rank + 1:
                crit_cons.append([v, w])
