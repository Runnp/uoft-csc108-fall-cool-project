def minSwaps(nums: list[int]) -> int:
        digit_sums = [sum(int(digit) for digit in str(num)) for num in nums]
        return(digit_sums)

print(minSwaps(nums = [13, 56, 75, 345, 2113]))
