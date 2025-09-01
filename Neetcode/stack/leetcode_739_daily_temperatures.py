# LeetCode 739 - Daily Temperatures (Medium)
#
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait
# after the i-th day to get a warmer temperature.
# If there is no future day for which this is possible, answer[i] = 0.
#
# Examples:
# Input:  temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
#
# Input:  temperatures = [30,40,50,60]
# Output: [1,1,1,0]
#
# Input:  temperatures = [30,60,90]
# Output: [1,1,0]
#
# Constraints:
# - 1 <= temperatures.length <= 10^5
# - 30 <= temperatures[i] <= 100
#
# Time complexity: O(n)
# Space complexity: O(n) 

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res


# -----------------------------
# Test cases for Daily Temperatures
# -----------------------------
def test_daily_temperatures():
    print("Running test cases for Daily Temperatures...")
    sol = Solution()

    # Example 1
    assert sol.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0], "Test 1 failed"

    # Example 2
    assert sol.dailyTemperatures([30,40,50,60]) == [1,1,1,0], "Test 2 failed"

    # Example 3
    assert sol.dailyTemperatures([30,60,90]) == [1,1,0], "Test 3 failed"

    # Edge cases
    assert sol.dailyTemperatures([100]) == [0], "Test 4 failed"              # single element
    assert sol.dailyTemperatures([70,70,70]) == [0,0,0], "Test 5 failed"    # all equal
    assert sol.dailyTemperatures([90,80,70,60]) == [0,0,0,0], "Test 6 failed" # strictly decreasing

    print("All test cases passed!")


if __name__ == "__main__":
    test_daily_temperatures()
