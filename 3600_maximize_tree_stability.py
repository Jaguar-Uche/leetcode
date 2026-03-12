from typing import List
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False

        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa

        self.parent[pb] = pa

        if self.rank[pa] == self.rank[pb]:
            self.rank[pa] += 1

        self.components -= 1
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=lambda x: -x[2])

        def check(mid):
            dsu = DSU(n)
            upgrades = 0

            # add forced edges
            for u, v, w, must in edges:
                if must == 1:
                    if w < mid:
                        return False
                    if not dsu.union(u, v):
                        return False

            # process optional edges
            for u, v, w, must in edges:
                if must == 0 and dsu.find(u) != dsu.find(v):

                    if w >= mid:
                        dsu.union(u, v)

                    elif 2 * w >= mid and upgrades < k:
                        dsu.union(u, v)
                        upgrades += 1

            return dsu.components == 1

        lo, hi = 0, max(e[2] for e in edges) * 2
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans

solution = Solution()
print(solution.maxStability(n = 3, edges = [[0,1,2,1],[1,2,3,0]], k = 1))
