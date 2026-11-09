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

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        dp = [{0}] + [set() for _ in range(len(grid[0]) - 1)]
        for row in grid:
            for j, v in enumerate(row):
                dp[j] = {x ^ v for x in dp[j] | (dp[j - 1] if j else set())}
        return min(dp[-1])


sm = (1 << (512))-1
swapmasks = [0]*9 + [sm]
for i in range(8, -1, -1):
    sm ^= sm << (1 << i)
    swapmasks[i] = sm

def swap_for(path, cell):
    for i in range(10):
        if cell & (1 << i):
            path = ((path & swapmasks[i]) << (1 << i)) | ((path & (swapmasks[i] << (1 << i))) >> (1 << i))
    return path

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        paths = [0]*n
        xor = grid[0][0]
        paths[0] = 1 << xor
        for c in range(1, n):
            xor ^= grid[0][c]
            paths[c] = 1 << xor
        xor = grid[0][0]
        for r in range(1, m):
            xor ^= grid[r][0]
            paths[0] = 1 << xor
            for c in range(1, n):
                paths[c] = swap_for(paths[c-1] | paths[c], grid[r][c])

        return (paths[n-1] & -paths[n-1]).bit_length() - 1

class Solution:
    def shortestPath(
        self, n: int, edges: List[List[int]], labels: str, k: int
    ) -> int:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))

        dis = [[2**31 - 1] * (k + 1) for _ in range(n)]
        # {shortest path length, node index, number of consecutive identical letters at the end}
        pq = []

        dis[0][1] = 0
        heappush(pq, (0, 0, 1))

        while pq:
            d, x, cnt = heappop(pq)

            if d > dis[x][cnt]:
                continue
            if x == n - 1:
                return d

            for y, w in g[x]:
                new_cnt = cnt + 1 if labels[x] == labels[y] else 1
                if new_cnt > k:
                    continue

                nd = d + w
                if nd < dis[y][new_cnt]:
                    dis[y][new_cnt] = nd
                    heappush(pq, (nd, y, new_cnt))

        return -1

class Solution:
    def shortestPath(
        self, n: int, edges: List[List[int]], labels: str, k: int
    ) -> int:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))

        dis = [[2**31 - 1] * (k + 1) for _ in range(n)]
        # {shortest path length, node index, number of consecutive identical letters at the end}
        pq = []

        dis[0][1] = 0
        heappush(pq, (0, 0, 1))

        while pq:
            d, x, cnt = heappop(pq)

            if d > dis[x][cnt]:
                continue
            if x == n - 1:
                return d

            for y, w in g[x]:
                new_cnt = cnt + 1 if labels[x] == labels[y] else 1
                if new_cnt > k:
                    continue

                nd = d + w
                if nd < dis[y][new_cnt]:
                    dis[y][new_cnt] = nd
                    heappush(pq, (nd, y, new_cnt))

        return -1

# Given an m x n binary grid grid where:
#
# grid[i][j] == 0 represents an empty cell, and
# grid[i][j] == 1 represents a mirror.
# A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). It can move only right or down. If the robot attempts to move into a mirror cell, it is reflected before entering that cell:
#
# If it tries to move right into a mirror, it is turned down and moved into the cell directly below the mirror.
# If it tries to move down into a mirror, it is turned right and moved into the cell directly to the right of the mirror.
# If this reflection would cause the robot to move outside the grid boundaries, the path is considered invalid and should not be counted.
#
# Return the number of unique valid paths from (0, 0) to (m - 1, n - 1).
#
# Since the answer may be very large, return it modulo 109 + 7.
#
# Note: If a reflection moves the robot into a mirror cell, the robot is immediately reflected again based on the direction it used to enter that mirror: if it entered while moving right, it will be turned down; if it entered while moving down, it will be turned right. This process will continue until either the last cell is reached, the robot moves out of bounds or the robot moves to a non-mirror cell.

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # f[i][j][0]: enter (i, j) by moving down
        # f[i][j][1]: enter (i, j) by moving right
        f = [[[0, 0] for _ in range(n)] for _ in range(m)]
        f[0][0][0] = 1

        for i in range(m):
            for j in range(n):
                if i > 0:
                    if grid[i - 1][j] == 0:
                        f[i][j][0] = f[i - 1][j][0] + f[i - 1][j][1]
                    else:
                        f[i][j][0] = f[i - 1][j][1]
                    f[i][j][0] %= MOD

                if j > 0:
                    if grid[i][j - 1] == 0:
                        f[i][j][1] = f[i][j - 1][0] + f[i][j - 1][1]
                    else:
                        f[i][j][1] = f[i][j - 1][0]
                    f[i][j][1] %= MOD

        return (f[m - 1][n - 1][0] + f[m - 1][n - 1][1]) % MOD


class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        curRow = [0] * n
        curRow[0] = 1
        for row in grid:
            prvRow, curRow, prvCel = curRow, [0] * n, 0

            for idx, p in enumerate(prvRow):
                if row[idx] == 0:
                    curRow[idx], prvCel = prvCel + p, prvCel + p
                else:
                    curRow[idx], prvCel = prvCel, p

        return curRow[-1] % 1_000_000_007


# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
#
# In one move, you can increment n - 1 elements of the array by 1.
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minimum = min(nums)
        return sum(n - minimum for n in nums)

# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
#
# In one move, you can increment or decrement an element of the array by 1.
#
# Test cases are designed so that the answer will fit in a 32-bit integer.
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 0
        nums.sort()
        mid = nums[l // 2]
        res = 0
        for i in nums:
            res += abs(i - mid)
        return res


# You are given an integer array nums and two integers, x and k. You can perform the following operation any number of times (including zero):
# Increase or decrease any element of nums by 1.
# Return the minimum number of operations needed to have at least k non-overlapping subarrays of size exactly x in nums, where all elements within each subarray are equal.

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        left, right = [], []
        delayed = defaultdict(int)
        left_size = right_size = 0
        sum_l = sum_r = 0
        ops = [0] * n

        def prune(h: List[int], sign: int) -> None:
            while h and delayed[sign * h[0]]:
                delayed[sign * h[0]] -= 1
                heappop(h)

        def balance() -> None:
            nonlocal left_size, right_size, sum_l, sum_r
            if left_size > right_size + 1:
                num = -heappop(left)
                heappush(right, num)
                sum_r += num
                sum_l -= num
                right_size += 1
                left_size -= 1
                prune(left, -1)
            elif right_size > left_size:
                num = heappop(right)
                heappush(left, -num)
                sum_l += num
                sum_r -= num
                left_size += 1
                right_size -= 1
                prune(right, 1)

        for i, num in enumerate(nums):
            if not left or num <= -left[0]:
                heappush(left, -num)
                left_size += 1
                sum_l += num
            else:
                heappush(right, num)
                right_size += 1
                sum_r += num
            balance()
            if i >= x:
                num = nums[i - x]
                delayed[num] += 1
                if num <= -left[0]:
                    left_size -= 1
                    sum_l -= num
                    if num == -left[0]:
                        prune(left, -1)
                else:
                    right_size -= 1
                    sum_r -= num
                    if num == right[0]:
                        prune(right, 1)
                balance()
            if i >= x - 1:
                mid = -left[0]
                ops[i] = sum_r - sum_l + mid * (left_size - right_size)

        dp = [[0] + [inf] * k for _ in range(n)]
        for j in range(1, k + 1):
            if j == 1:
                dp[x - 1][j] = ops[x - 1]
            else:
                dp[j * x - 1][j] = dp[(j - 1) * x - 1][j - 1] + ops[j * x - 1]
        for j in range(1, k + 1):
            for i in range(j * x, n):
                dp[i][j] = min(dp[i - x][j - 1] + ops[i], dp[i - 1][j])
        return dp[n - 1][k]

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        free = list(range(k))

        handled, busy = [], []
        for i, (t, d) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= t:
                heappush(free, i + (heappop(busy)[1] - i) % k)
            if free:
                x = heappop(free) % k
                heappush(busy, (t + d, x))
                handled.append(x)

        return multimode(handled)

# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.
#
# Return the number of servers that communicate with any other server.

