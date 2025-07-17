# LeetCode 26 - Remove Duplicates from Sorted Array (Easy)
#
# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
#
# Return k — the number of unique elements. The first k elements of nums must contain
# the unique elements in the same relative order. The remaining elements do not matter.
#
# Example 1:
# Input:  nums = [1,1,2]
# Output: 2, nums = [1,2,_]
#
# Example 2:
# Input:  nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
#
# Constraints:
# - 1 <= nums.length <= 3 * 10^4
# - -100 <= nums[i] <= 100
# - nums is sorted in non-decreasing order
#
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l

# Test
def test_remove_duplicates():
    s = Solution()

    nums1 = [1, 1, 2]
    k1 = s.removeDuplicates(nums1)
    print(k1, nums1[:k1])  # Output: 2, [1, 2]

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = s.removeDuplicates(nums2)
    print(k2, nums2[:k2])  # Output: 5, [0, 1, 2, 3, 4]

    nums3 = [1, 2, 3, 4, 5]
    k3 = s.removeDuplicates(nums3)
    print(k3, nums3[:k3])  # Output: 5, [1, 2, 3, 4, 5]

    nums4 = [1, 1, 1, 1]
    k4 = s.removeDuplicates(nums4)
    print(k4, nums4[:k4])  # Output: 1, [1]

test_remove_duplicates()
