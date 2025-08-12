# LeetCode 153 - Find Minimum in Rotated Sorted Array (Medium)
#
# Given a rotated sorted array with unique elements, find the minimum element.
# Must run in O(log n) time complexity.
#
# Examples:
# Input: nums = [3,4,5,1,2]       -> Output: 1
# Input: nums = [4,5,6,7,0,1,2]   -> Output: 0
# Input: nums = [11,13,15,17]     -> Output: 11
#
# Time complexity: O(log n)
# Space complexity: O(1)

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        minimum = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                minimum = mid
                right = mid - 1
            else:
                left = mid + 1
        return nums[minimum]


# Test cases for Find Minimum in Rotated Sorted Array
def test_find_min():
    print("Running test cases for Find Minimum in Rotated Sorted Array...")
    sol = Solution()

    assert sol.findMin([3,4,5,1,2]) == 1, "Test 1 failed"
    assert sol.findMin([4,5,6,7,0,1,2]) == 0, "Test 2 failed"
    assert sol.findMin([11,13,15,17]) == 11, "Test 3 failed"
    assert sol.findMin([2,3,4,5,6,7,1]) == 1, "Test 4 failed"
    assert sol.findMin([1]) == 1, "Test 5 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_find_min()
