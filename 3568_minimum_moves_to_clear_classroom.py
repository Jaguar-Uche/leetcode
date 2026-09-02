from typing import List
from collections import deque

def find_starting_position_string(grid:List[str]):
    n = len(grid)
    m = len(grid[0])
    litter_positions = {}
    start_x, start_y = 0,0
    litter_seen = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "S":
                start_x, start_y =  i, j
            elif grid[i][j] == "L":
                litter_positions[(i,j)] = litter_seen
                litter_seen += 1
    return (start_x, start_y), litter_positions

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        n = len(classroom)
        h = len(classroom[0])
        (start_x, start_y), litter_positions = find_starting_position_string(grid=classroom)
        litter_no = len(litter_positions)
        if litter_no == 0:
            return 0
        full_mask = (1 << litter_no) - 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        best_energy = {(start_x, start_y, 0): energy}
        queue = deque([(start_x, start_y, 0, energy, 0)])
        while queue:
            (x,y, m, e, s) = queue.popleft()
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                new_e = e -1
                new_s = s+1
                new_m = m
                if not (0 <= new_x < n and 0 <= new_y < h):
                    continue
                if new_e < 0:
                    continue
                cell = classroom[new_x][new_y]
                if cell == "R":
                    new_e = energy
                elif cell == "L":
                    litter_id = litter_positions[(new_x, new_y)]
                    new_m |= (1 << litter_id)
                    if new_m == full_mask:
                        return new_s
                elif cell == "X":
                    continue
                previous_energy = best_energy.get((new_x, new_y, new_m), -1)
                if previous_energy < new_e:
                    best_energy[(new_x, new_y, new_m)] = new_e
                    queue.append((new_x, new_y, new_m, new_e, new_s))
        return -1
sol = Solution()
print(sol.minMoves(classroom = ["L.S", "RXL"], energy = 3))
