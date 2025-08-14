# LeetCode 35 - Search Insert Position (Easy)
#
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Examples:
# Input: nums = [1,3,5,6], target = 5  -> Output: 2
# Input: nums = [1,3,5,6], target = 2  -> Output: 1
# Input: nums = [1,3,5,6], target = 7  -> Output: 4
#
# Time complexity: O(log n)
# Space complexity: O(1)

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        boundary_index = len(nums)

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                boundary_index = mid
                r = mid - 1

        return boundary_index


# Test cases for Search Insert Position
def test_search_insert_position():
    print("Running test cases for Search Insert Position...")
    sol = Solution()

    assert sol.searchInsert([1,3,5,6], 5) == 2, "Test 1 failed"
    assert sol.searchInsert([1,3,5,6], 2) == 1, "Test 2 failed"
    assert sol.searchInsert([1,3,5,6], 7) == 4, "Test 3 failed"
    assert sol.searchInsert([1,3,5,6], 0) == 0, "Test 4 failed"
    assert sol.searchInsert([1], 0) == 0, "Test 5 failed"
    assert sol.searchInsert([1], 2) == 1, "Test 6 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_search_insert_position()
