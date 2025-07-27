# LeetCode 20 - Valid Parentheses (Easy)
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# A string is valid if:
# - Open brackets are closed by the same type of brackets.
# - Open brackets are closed in the correct order.
# - Every closing bracket has a corresponding open bracket of the same type.
#
# Example:
# Input:  s = "()[]{}"
# Output: True
#
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_to_close = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in open_to_close:
                if stack and stack[-1] == open_to_close[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack


# Test
def test_is_valid():
    s = Solution()

    print(s.isValid("()"))         # True
    print(s.isValid("()[]{}"))     # True
    print(s.isValid("(]"))         # False
    print(s.isValid("([])"))       # True
    print(s.isValid("([)]"))       # False
    print(s.isValid("["))          # False

test_is_valid()
