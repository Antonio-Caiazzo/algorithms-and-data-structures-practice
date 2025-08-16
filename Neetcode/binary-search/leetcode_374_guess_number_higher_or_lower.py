# LeetCode 374 - Guess Number Higher or Lower (Easy)
#
# We play a game where the API `guess(num)` tells us if our guess is
# lower (-1 means our guess is higher than pick, 1 means lower, 0 means equal).
# Return the picked number in [1..n].
#
# Time complexity: O(log n)
# Space complexity: O(1)

from typing import Optional

# On LeetCode, `guess` is provided by the environment.
# Here we define a placeholder so the file can be tested locally with a mock.
def guess(num: int) -> int:  # type: ignore[func-returns-value]
    raise NotImplementedError("LeetCode provides this function at runtime")


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            res = guess(mid) 
            if res == 0:
                return mid
            elif res < 0:      
                r = mid - 1
            else:             
                l = mid + 1
        return -1


# -----------------------------
# Local tests (with a mock API)
# -----------------------------
class _GuessGame:
    def __init__(self, pick: int):
        self.pick = pick
    def guess(self, num: int) -> int:
        if num > self.pick: return -1
        if num < self.pick: return 1
        return 0

def test_guess_number():
    print("Running test cases for Guess Number Higher or Lower...")
    # Monkey-patch the global `guess` with our mock for local tests
    global guess

    # Case 1
    game = _GuessGame(pick=6)
    guess = game.guess
    assert Solution().guessNumber(10) == 6, "Test 1 failed"

    # Case 2
    game = _GuessGame(pick=1)
    guess = game.guess
    assert Solution().guessNumber(1) == 1, "Test 2 failed"

    # Case 3
    game = _GuessGame(pick=1)
    guess = game.guess
    assert Solution().guessNumber(2) == 1, "Test 3 failed"

    # Extra
    game = _GuessGame(pick=2_000_000_000)
    guess = game.guess
    assert Solution().guessNumber(2_147_483_647) == 2_000_000_000, "Test 4 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_guess_number()
