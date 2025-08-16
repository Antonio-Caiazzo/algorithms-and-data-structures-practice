# LeetCode 69 - Sqrt(x) (Easy)
#
# Given a non-negative integer x, return the square root of x rounded down
# to the nearest integer. The returned integer should also be non-negative.
#
# You must not use any built-in exponent function or operator.
#
# Examples:
# Input: x = 4  -> Output: 2
# Input: x = 8  -> Output: 2
#
# Time complexity: O(log x)
# Space complexity: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        ans = 0

        while l <= r:
            mid = (l + r) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square > x:
                r = mid - 1
                ans = r
            else:
                l = mid + 1

        return ans


# -----------------------------
# Test cases for mySqrt
# -----------------------------
def test_my_sqrt():
    print("Running test cases for mySqrt...")
    sol = Solution()

    assert sol.mySqrt(4) == 2, "Test 1 failed"
    assert sol.mySqrt(8) == 2, "Test 2 failed"
    assert sol.mySqrt(0) == 0, "Test 3 failed"
    assert sol.mySqrt(1) == 1, "Test 4 failed"
    assert sol.mySqrt(15) == 3, "Test 5 failed"
    assert sol.mySqrt(100) == 10, "Test 6 failed"
    assert sol.mySqrt(999) == 31, "Test 7 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_my_sqrt()
