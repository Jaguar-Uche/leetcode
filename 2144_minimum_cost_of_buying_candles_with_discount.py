from typing import List
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        total_cost = 0
        n = len(cost)
        for i in range(1,n+1):
            if i % 3 == 0:
                continue
            else:
                total_cost += cost[n - i]
        return total_cost

solution = Solution()
print(solution.minimumCost([5,5]))

