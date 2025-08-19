# LeetCode 150 - Evaluate Reverse Polish Notation (Medium)
#
# You are given an array of strings tokens representing an arithmetic expression
# in Reverse Polish Notation. Evaluate the expression and return the result.
#
# The valid operators are "+", "-", "*", and "/".
# - Each operand may be an integer or another expression.
# - Division between two integers always truncates toward zero.
# - No division by zero occurs.
# - The input represents a valid RPN expression.
#
# Example 1:
# Input:  tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#
# Example 2:
# Input:  tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#
# Example 3:
# Input:  tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation:
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 22
#
# Constraints:
# - 1 <= tokens.length <= 10^4
# - tokens[i] is either an operator ("+", "-", "*", "/") or an integer in range [-200, 200].
#
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]


# Test cases for Evaluate Reverse Polish Notation
def test_eval_rpn():
    print("Running test cases for Evaluate Reverse Polish Notation...")
    sol = Solution()

    assert sol.evalRPN(["2","1","+","3","*"]) == 9, "Test 1 failed"
    assert sol.evalRPN(["4","13","5","/","+"]) == 6, "Test 2 failed"
    assert sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22, "Test 3 failed"

    # Extra cases
    assert sol.evalRPN(["3","4","+"]) == 7, "Test 4 failed"
    assert sol.evalRPN(["5","1","2","+","4","*","+","3","-"]) == 14, "Test 5 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_eval_rpn()
