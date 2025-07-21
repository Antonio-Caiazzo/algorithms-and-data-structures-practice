# LeetCode 1 - Two Sum (Easy)
#
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# Each input has exactly one solution, and you may not use the same element twice.

# Example:
# Input:  nums = [2,7,11,15], target = 9
# Output: [0,1]  (Because nums[0] + nums[1] == 9)

# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in m:
                return [m[x], i]
            else:
                m[num] = i

# Test
def test_two_sum():
    s = Solution()

    print(s.twoSum([2, 7, 11, 15], 9))   # Output: [0, 1]
    print(s.twoSum([3, 2, 4], 6))        # Output: [1, 2]
    print(s.twoSum([3, 3], 6))           # Output: [0, 1]

test_two_sum()
