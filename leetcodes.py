class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        target = sorted(nums, key=lambda x: (sum(int(d) for d in str(x)), x))
        pos = {val: i for i, val in enumerate(target)}
        vis = [False] * len(nums)
        swap_count = 0
        for i in range(len(nums)):
            if vis[i] or pos[nums[i]] == i:
                continue
            cycle_size = 0
            j = i
            while not vis[j]:
                vis[j] = True
                j = pos[nums[j]]
                cycle_size += 1
            if cycle_size > 0:
                swap_count += (cycle_size - 1)
        return swap_count

# You are given a string s consisting of lowercase English letters.
#
# In one operation, you can select any substring of s that is not the entire string and sort it in non-descending alphabetical order.
#
# Return the minimum number of operations required to make s sorted in non-descending order. If it is not possible, return -1.

class Solution:
    def minOperations(self, s: str) -> int:
        m, n = max(s), min(s)
        if all(a <= b for a, b in zip(s, s[1:])):
            return 0
        if len(s) == 2:
            return -1
        if s[0] == n or s[-1] == m:
            return 1
        for i in range(1, len(s) - 1):
            if s[i] == n or s[i] == m:
                return 2
        return 3

# s = "dcba"
# start = 1
# end = 4
# s = s[:start] + ''.join(sorted(s[start:end])) + s[end:]
# print(s)

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        m = -1
        for i, x in enumerate(nums):
            if x != i:
                m &= x
                if not m:
                    return 0
        return max(m, 0)


# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
#
# Return the number of closed islands.

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def closed(i, j):
            if not (0 <= i < m and 0 <= j < n):
                return False
            if grid[i][j]:
                return True
            grid[i][j] = 1
            return closed(i + 1, j) & closed(i - 1, j) & closed(i, j + 1) & closed(i, j - 1)

        return sum(closed(i, j) for i in range(m) for j in range(n) if not grid[i][j])

# You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).
# The total value of an island is the sum of the values of all cells in the island.
# Return the number of islands with a total value divisible by k.
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                total, grid[i][j], island = grid[i][j], 0, [(i, j)]
                for x, y in island:
                    for a, b in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                        if 0 <= a < m and 0 <= b < n and grid[a][b]:
                            total += grid[a][b]
                            grid[a][b] = 0
                            island.append((a, b))
                ans += total % k == 0
        return ans


# You are given two integers m and n, representing the number of rows and columns of a grid.
#
# Construct any m x n grid consisting only of the characters '.' and '#', where:
#
# '.' represents a free cell.
# '#' represents an obstacle cell.
# A valid path is a sequence of free cells that:
#
# Starts at the top-left cell (0, 0).
# Ends at the bottom-right cell (m - 1, n - 1).
# Moves only:
# Right, from (i, j) to (i, j + 1), or
# Down, from (i, j) to (i + 1, j).
# Return any grid such that there is exactly one valid path from the top-left cell to the bottom-right cell.

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = [['#'] * n for _ in range(m)]
        r = c = 0

        res[r][c] = '.'

        while r < m - 1 or c < n - 1:
            if r < m - 1 and (
                    c == n - 1 or abs((r + 1) * (n - 1) - c * (m - 1)) <= abs(r * (n - 1) - (c + 1) * (m - 1))):
                r += 1
            else:
                c += 1

            res[r][c] = '.'

        return [''.join(row) for row in res]


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        arr = [("." + "#" * (n - 1)) for i in range(m - 1)]
        arr.append("." * n)

        return arr

# Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.
class Solution:
    def maxDepth(self, s):
        depth = 0
        r = 0
        for c in s:
            if c == ')':
                depth -= 1
                continue
            if c != '(':
                continue
            depth += 1
            if depth > r:
                r = depth
        return r

# You are given a 2D integer array grid of size m * n.
#
# You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).
#
# At each step, you may move either right or down.
#
# The cost of a path is defined as the bitwise XOR of all the values in the cells along that path, including the start and end cells.
#
# Return the minimum possible XOR value among all valid paths from (0, 0) to (m - 1, n - 1).