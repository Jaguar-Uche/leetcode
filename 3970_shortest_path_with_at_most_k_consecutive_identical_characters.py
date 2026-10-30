from typing import List
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # dist[node][consecutive_count]
        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        # Starting at node 0, its character already counts as 1
        dist[0][1] = 0

        heap = [(0, 0, 1)]  # cost, node, consecutive_count

        while heap:
            cost, node, count = heapq.heappop(heap)

            if cost > dist[node][count]:
                continue

            if node == n - 1:
                return cost

            for nei, weight in graph[node]:

                if labels[nei] == labels[node]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + weight

                if new_cost < dist[nei][new_count]:
                    dist[nei][new_count] = new_cost

                    heapq.heappush(
                        heap,
                        (new_cost, nei, new_count)
                    )

        return -1