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