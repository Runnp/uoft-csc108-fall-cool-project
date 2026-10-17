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
