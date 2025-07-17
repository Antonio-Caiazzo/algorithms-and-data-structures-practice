# LeetCode 680 - Valid Palindrome II (Easy)
#
# Given a string s, return true if the string can be a palindrome after deleting at most one character.
#
# Example 1:
# Input:  s = "aba"
# Output: true
#
# Example 2:
# Input:  s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
#
# Example 3:
# Input:  s = "abc"
# Output: false
#
# Constraints:
# - 1 <= s.length <= 10^5
# - s consists of lowercase English letters
#
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        while l < r:
            if s[l] != s[r]:
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
            l, r = l + 1, r - 1
        return True

# Test
def test_valid_palindrome():
    s = Solution()

    print(s.validPalindrome("aba"))   # Output: True
    print(s.validPalindrome("abca"))  # Output: True
    print(s.validPalindrome("abc"))   # Output: False
    print(s.validPalindrome("deeee")) # Output: True
    print(s.validPalindrome("eeccdceew"))  # Output: False

test_valid_palindrome()
