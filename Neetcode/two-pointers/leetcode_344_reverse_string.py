# LeetCode 344 - Reverse String (Easy)
#
# Write a function that reverses a string. The input string is given as an array
# of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
#
# Example 1:
# Input:  s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#
# Example 2:
# Input:  s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#
# Constraints:
# - 1 <= s.length <= 10^5
# - s[i] is a printable ascii character
#
# Time complexity: O(n)
# Space complexity: O(1)
# (In-place, constant extra space)

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

# Test
s1 = ["h", "e", "l", "l", "o"]
Solution().reverseString(s1)
print(s1)  # Output: ["o", "l", "l", "e", "h"]

s2 = ["H", "a", "n", "n", "a", "h"]
Solution().reverseString(s2)
print(s2)  # Output: ["h", "a", "n", "n", "a", "H"]

s3 = ["a"]
Solution().reverseString(s3)
print(s3)  # Output: ["a"]

s4 = ["a", "b"]
Solution().reverseString(s4)
print(s4)  # Output: ["b", "a"]
