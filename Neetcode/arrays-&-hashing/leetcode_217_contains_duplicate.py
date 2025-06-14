# LeetCode 217 - Contains Duplicate (Easy)
# 
# Given an integer array `nums`, return True if any value appears at least twice,
# and return False if every element is distinct.
#
# Example:
#   Input:  nums = [1, 2, 3, 1]
#   Output: True

# Time complexity: O(n)
# Space complexity: O(n)
from typing import List
def containsDuplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))

# Test
print(containsDuplicate([1, 2, 3, 1]))  # Output: True
print(containsDuplicate([1, 2, 3, 4]))  # Output: False
print(containsDuplicate([]))           # Output: False
print(containsDuplicate([7, 7, 7]))     # Output: True
