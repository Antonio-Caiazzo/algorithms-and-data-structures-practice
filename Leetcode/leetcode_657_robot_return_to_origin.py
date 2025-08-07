# LeetCode 657 - Robot Return to Origin (Easy)
#
# There is a robot starting at (0, 0) on a 2D plane.
# Given a string `moves` consisting of 'R', 'L', 'U', and 'D',
# return True if the robot returns to the origin after completing all moves,
# and False otherwise.
#
# Example:
# Input: moves = "UD"
# Output: True
#
# Constraints:
# - 1 <= moves.length <= 2 * 10^4
# - moves only contains the characters 'U', 'D', 'L', 'R'
#
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horizontal_position = 0
        vertical_position = 0

        for move in moves:
            if move == 'R':
                horizontal_position += 1
            elif move == 'L':
                horizontal_position -= 1
            elif move == 'U':
                vertical_position += 1
            elif move == 'D':
                vertical_position -= 1

        return horizontal_position == 0 and vertical_position == 0


# Test cases for judgeCircle
def test_judge_circle():
    print("Running test cases for judgeCircle...")
    sol = Solution()
    assert sol.judgeCircle("UD") == True, "Test case 1 failed"
    assert sol.judgeCircle("LL") == False, "Test case 2 failed"
    assert sol.judgeCircle("UDLR") == True, "Test case 3 failed"
    assert sol.judgeCircle("RRDDLU") == False, "Test case 4 failed"
    assert sol.judgeCircle("UDUDUDUD") == True, "Test case 5 failed"
    print("All test cases passed!")


if __name__ == "__main__":
    test_judge_circle()
