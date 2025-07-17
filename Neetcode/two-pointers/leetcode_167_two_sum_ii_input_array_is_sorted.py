# LeetCode 167 - Two Sum II - Input Array Is Sorted (Medium)
#
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
#
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2].
# Your solution must use only constant extra space.
#
# Example 1:
# Input:  numbers = [2,7,11,15], target = 9
# Output: [1,2]
#
# Example 2:
# Input:  numbers = [2,3,4], target = 6
# Output: [1,3]
#
# Example 3:
# Input:  numbers = [-1,0], target = -1
# Output: [1,2]
#
# Constraints:
# - 2 <= numbers.length <= 3 * 10^4
# - -1000 <= numbers[i] <= 1000
# - numbers is sorted in non-decreasing order.
# - -1000 <= target <= 1000
# - The tests are generated such that there is exactly one solution.
#
# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return []

# Test
def test_two_sum():
    s = Solution()

    nums1 = [2, 7, 11, 15]
    print(s.twoSum(nums1, 9))  # Output: [1, 2]

    nums2 = [2, 3, 4]
    print(s.twoSum(nums2, 6))  # Output: [1, 3]

    nums3 = [-1, 0]
    print(s.twoSum(nums3, -1))  # Output: [1, 2]

    nums4 = [1, 3, 4, 5, 7, 10, 11]
    print(s.twoSum(nums4, 9))  # Output: [3, 4]

test_two_sum()
