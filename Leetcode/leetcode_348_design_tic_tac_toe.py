# LeetCode 348 - Design Tic-Tac-Toe (Medium)
#
# Design a Tic-tac-toe game played on an n x n grid between two players.
# Each move is valid and placed on an empty cell. A player wins by placing
# n of their marks in a row (horizontal, vertical, or diagonal).
#
# Your implementation should support:
# - TicTacToe(int n): constructor to initialize the game
# - move(int row, int col, int player): returns the winner (1 or 2) or 0 if no one wins yet
#
# Optimization: O(1) per move using counters instead of storing the full board
#
# Time complexity: O(1) 
# Space complexity: O(n)

class TicTacToe:
    def __init__(self, n: int):
        self.board_size = n
        # counters[player][0..n-1] => rows
        # counters[player][n..2n-1] => columns
        # counters[player][2n] => main diagonal
        # counters[player][2n+1] => anti-diagonal
        self.counters = [[0] * (2 * n + 2) for _ in range(2)]

    def move(self, row: int, col: int, player: int) -> int:
        player_index = player - 1
        diagonal_index = 2 * self.board_size
        anti_diagonal_index = 2 * self.board_size + 1

        self.counters[player_index][row] += 1
        self.counters[player_index][col + self.board_size] += 1
        if row == col:
            self.counters[player_index][diagonal_index] += 1
        if row + col == self.board_size - 1:
            self.counters[player_index][anti_diagonal_index] += 1

        if (
            self.counters[player_index][row] == self.board_size
            or self.counters[player_index][col + self.board_size] == self.board_size
            or self.counters[player_index][diagonal_index] == self.board_size
            or self.counters[player_index][anti_diagonal_index] == self.board_size
        ):
            return player
        return 0


# Test cases for TicTacToe
def test_tic_tac_toe():
    print("Running test cases for TicTacToe...")
    toe = TicTacToe(3)
    assert toe.move(0, 0, 1) == 0, "Test 1 failed"
    assert toe.move(0, 2, 2) == 0, "Test 2 failed"
    assert toe.move(2, 2, 1) == 0, "Test 3 failed"
    assert toe.move(1, 1, 2) == 0, "Test 4 failed"
    assert toe.move(2, 0, 1) == 0, "Test 5 failed"
    assert toe.move(1, 0, 2) == 0, "Test 6 failed"
    assert toe.move(2, 1, 1) == 1, "Test 7 failed"
    print("All test cases passed!")


if __name__ == "__main__":
    test_tic_tac_toe()
