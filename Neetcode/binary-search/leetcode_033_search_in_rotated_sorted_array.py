# LeetCode 33 - Search in Rotated Sorted Array (Medium)
#
# There is an integer array nums sorted in ascending order (distinct values),
# possibly rotated at an unknown index k. Given nums and an integer target,
# return the index of target if present; otherwise return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Examples:
# Input: nums = [4,5,6,7,0,1,2], target = 0  -> Output: 4
# Input: nums = [4,5,6,7,0,1,2], target = 3  -> Output: -1
# Input: nums = [1], target = 0               -> Output: -1
#
# Time complexity: O(log n)
# Space complexity: O(1)

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else: 
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


# Test cases for Search in Rotated Sorted Array
def test_search_in_rotated_sorted_array():
    print("Running test cases for Search in Rotated Sorted Array...")
    sol = Solution()

    # Provided examples
    assert sol.search([4,5,6,7,0,1,2], 0) == 4, "Test 1 failed"
    assert sol.search([4,5,6,7,0,1,2], 3) == -1, "Test 2 failed"
    assert sol.search([1], 0) == -1, "Test 3 failed"

    # Extra coverage
    assert sol.search([6,7,8,1,2,3,4,5], 6) == 0, "Test 4 failed"
    assert sol.search([6,7,8,1,2,3,4,5], 5) == 7, "Test 5 failed"
    assert sol.search([1,3], 3) == 1, "Test 6 failed"
    assert sol.search([3,1], 1) == 1, "Test 7 failed"
    assert sol.search([5,1,3], 3) == 2, "Test 8 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_search_in_rotated_sorted_array()
