# LeetCode 15 - 3Sum (Medium)
#
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# The solution set must not contain duplicate triplets.
#
# Example 1:
# Input:  nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#
# Example 2:
# Input:  nums = [0,1,1]
# Output: []
#
# Example 3:
# Input:  nums = [0,0,0]
# Output: [[0,0,0]]
#
# Constraints:
# - 3 <= nums.length <= 3000
# - -10^5 <= nums[i] <= 10^5
#
# Time complexity: O(n^2)
# Space complexity: O(1) (excluding output list)

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                sum_zero = a + nums[l] + nums[r]
                if sum_zero > 0:
                    r -= 1
                elif sum_zero < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res


# Test
def test_three_sum():
    s = Solution()

    print(s.threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
    print(s.threeSum([0, 1, 1]))              # Output: []
    print(s.threeSum([0, 0, 0]))              # Output: [[0, 0, 0]]
    print(s.threeSum([1, -1, -1, 0]))         # Output: [[-1, 0, 1]]
    print(s.threeSum([-2, 0, 1, 1, 2]))       # Output: [[-2, 0, 2], [-2, 1, 1]]

test_three_sum()
