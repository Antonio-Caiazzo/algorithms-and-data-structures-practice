# LeetCode 867 - Transpose Matrix (Easy)
#
# Given a 2D integer array `matrix`, return the **transpose** of `matrix`.
# The transpose of a matrix is the matrix flipped over its main diagonal,
# switching the row and column indices.
#
# Example:
# Input:  matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
#
# Time complexity: O(n * m)
# Space complexity: O(n * m), where n = number of rows, m = number of columns

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[j][i] = matrix[i][j]
        return result


# Test cases for transpose
def test_transpose_matrix():
    print("Running test cases for transpose...")
    sol = Solution()
    
    assert sol.transpose([[1,2,3],[4,5,6],[7,8,9]]) == [
        [1,4,7],
        [2,5,8],
        [3,6,9]
    ], "Test case 1 failed"
    
    assert sol.transpose([[1,2,3],[4,5,6]]) == [
        [1,4],
        [2,5],
        [3,6]
    ], "Test case 2 failed"

    assert sol.transpose([[1]]) == [[1]], "Test case 3 failed"

    assert sol.transpose([[1,2]]) == [[1],[2]], "Test case 4 failed"

    assert sol.transpose([[1],[2]]) == [[1,2]], "Test case 5 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_transpose_matrix()
