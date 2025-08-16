# LeetCode 682 - Baseball Game (Easy)
#
# You are given a list of strings `operations` representing a sequence of baseball operations:
#
# - Integer x: Record a new score of x.
# - "+": Record a new score that is the sum of the previous two scores.
# - "D": Record a new score that is double the previous score.
# - "C": Invalidate the previous score, removing it from the record.
#
# Return the sum of all the scores after performing all operations.
#
# Example:
# Input: ops = ["5","2","C","D","+"]
# Output: 30
#
# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == "C":
                stack.pop()
            elif operation == "D":
                stack.append(stack[-1] * 2)
            elif operation == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(operation))
        return sum(stack)


# -----------------------------
# Test cases for Baseball Game
# -----------------------------
def test_cal_points():
    print("Running test cases for Baseball Game...")
    sol = Solution()

    assert sol.calPoints(["5", "2", "C", "D", "+"]) == 30, "Test 1 failed"
    assert sol.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27, "Test 2 failed"
    assert sol.calPoints(["1"]) == 1, "Test 3 failed"
    assert sol.calPoints(["10", "20", "+", "D"]) == 120, "Test 4 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_cal_points()
