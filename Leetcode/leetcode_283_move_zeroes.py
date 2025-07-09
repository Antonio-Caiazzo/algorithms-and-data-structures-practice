# LeetCode 283 - Move Zeroes (Easy)
#
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
# You must do this in-place without making a copy of the array.
#
# Example 1:
# Input:  nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Example 2:
# Input:  nums = [0]
# Output: [0]
#
# Constraints:
# - 1 <= nums.length <= 10^4
# - -2^31 <= nums[i] <= 2^31 - 1
#
# Time complexity: O(n)
# Space complexity: O(1)
# (In-place, constant extra space)

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                if l != r:
                    nums[l], nums[r] = nums[r], nums[l]
                l += 1

# Test
nums1 = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums1)
print(nums1)  # Output: [1, 3, 12, 0, 0]

nums2 = [0]
Solution().moveZeroes(nums2)
print(nums2)  # Output: [0]

nums3 = [1, 2, 3]
Solution().moveZeroes(nums3)
print(nums3)  # Output: [1, 2, 3]

nums4 = [0, 0, 1]
Solution().moveZeroes(nums4)
print(nums4)  # Output: [1, 0, 0]

nums5 = [4, 0, 5, 0, 6, 0]
Solution().moveZeroes(nums5)
print(nums5)  # Output: [4, 5, 6, 0, 0, 0]
