# LeetCode 125 - Valid Palindrome (Easy)
#
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
#
# Return true if the given string is a palindrome, false otherwise.
#
# Example 1:
# Input:  s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
# Example 2:
# Input:  s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
# Example 3:
# Input:  s = " "
# Output: true
# Explanation: After removing non-alphanumeric characters, it becomes an empty string "".
# An empty string is considered a valid palindrome.
#
# Constraints:
# - 1 <= s.length <= 2 * 10^5
# - s consists only of printable ASCII characters
#
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c: str) -> bool:
        return (
            ord("A") <= ord(c) <= ord("Z") or
            ord("a") <= ord(c) <= ord("z") or
            ord("0") <= ord(c) <= ord("9")
        )

# Test
def test_is_palindrome():
    s = Solution()

    print(s.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
    print(s.isPalindrome("race a car"))                      # Output: False
    print(s.isPalindrome(" "))                               # Output: True
    print(s.isPalindrome("ab@a"))                            # Output: True
    print(s.isPalindrome("0P"))                              # Output: False

test_is_palindrome()
