# LeetCode 704 - Binary Search (Easy)
#
# Given a sorted (ascending) array 'nums' and an integer 'target',
# return the index of 'target' if present, otherwise return -1.
#
# Requirements: O(log n) time complexity.
#
# Examples:
# Input: nums = [-1,0,3,5,9,12], target = 9  -> Output: 4
# Input: nums = [-1,0,3,5,9,12], target = 2  -> Output: -1
#
# Time complexity: O(log n)
# Space complexity: O(1)

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


# Test cases for Binary Search
def test_binary_search():
    print("Running test cases for Binary Search...")
    sol = Solution()

    assert sol.search([-1,0,3,5,9,12], 9) == 4, "Test 1 failed"
    assert sol.search([-1,0,3,5,9,12], 2) == -1, "Test 2 failed"
    assert sol.search([5], 5) == 0, "Test 3 failed"
    assert sol.search([5], -1) == -1, "Test 4 failed"
    assert sol.search([1,2,3,4,5,6,7], 1) == 0, "Test 5 failed"
    assert sol.search([1,2,3,4,5,6,7], 7) == 6, "Test 6 failed"
    assert sol.search([1,3,5,7,9], 8) == -1, "Test 7 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_binary_search()
