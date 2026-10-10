# class Solution:
#     def minInsertions(self, s: str) -> int:
#         insertions = 0
#         need = 0
#
#         for char in s:
#             if char == '(':
#                 if need % 2 == 1:
#                     insertions += 1
#                     need -= 1
#
#                 need += 2
#
#             else:
#                 need -= 1
#
#                 if need == -1:
#                     insertions += 1
#                     need = 1
#
#         return insertions + need

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # if k1 == 0 and k2 == 0:
        #     for i in nums1 and i in nums2:
        #         c = nums1[i] - nums2[i]
        #         v += (c ** c)
        #     return (v)
        # else:
        #     for n in nums1 and n in nums2:
        #         if n == nums1[0]:
        #             n += 1
        #         if n == nums2[2]:
        #             n += 1
        #         r = (nums1[n] - nums2[n]) ** 2
        #     return r
        differences = [
            abs(nums1[i] - nums2[i])
            for i in range(len(nums1))
        ]
        k = k1 + k2

        if k >= sum(differences):
            return 0

        left = 0
        right = max(differences)

        while left < right:
            cap = (left + right) // 2

            needed = sum(
                max(d - cap, 0)
                for d in differences
            )

            if needed <= k:
                right = cap
            else:
                left = cap + 1

        cap = left
        used = 0
        answer = 0

        for d in differences:
            reduced = min(d, cap)
            used += d - reduced
            answer += reduced ** 2

        remaining = k - used
        saving_per_operation = cap ** 2 - (cap - 1) ** 2

        answer -= remaining * saving_per_operation

        return answer