# LeetCode 853 - Car Fleet (Medium)
#
# Given the target mile and arrays of starting positions and speeds for n cars,
# return the number of car fleets that will arrive at the destination.
# A car cannot pass another car. If a car catches a slower car (or fleet),
# it becomes part of that fleet and travels at the slowest speed of the fleet.
# If catch-up happens exactly at target, it still counts as the same fleet.
#
# Examples:
# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3] -> Output: 3
# Input: target = 10, position = [3], speed = [3]                  -> Output: 1
# Input: target = 100, position = [0,2,4], speed = [4,2,1]         -> Output: 1
#
# Constraints:
# - n == position.length == speed.length
# - 1 <= n <= 1e5
# - 0 < target <= 1e6
# - 0 <= position[i] < target
# - All position values are unique
# - 0 < speed[i] <= 1e6
#
# Approach (iterative, one-pass after sorting):
#   Sort cars by starting position descending (closest to target first).
#   Compute each car's time to reach target: t = (target - pos) / speed.
#   Maintain the maximum "front" time seen so far (slowest fleet ahead).
#   If current t > max_time, it forms a new fleet; else it merges into the fleet ahead.
#
# Time complexity:  O(n log n) 
# Space complexity: O(n)
#
# Alternative (stack) approach:
#   Push times from right to left; pop/merge when the new time <= top of stack.
#   Time: O(n log n), Space: O(n). Implemented as an auxiliary method below.

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        front_time = float("-inf")  

        for pos, sp in cars:
            t = (target - pos) / sp
            if t > front_time:
                fleets += 1
                front_time = t  
        return fleets

    def carFleet_stack(self, target: int, position: List[int], speed: List[int]) -> int:
        stack: List[float] = []
        for p, s in sorted(zip(position, speed))[::-1]:
            t = (target - p) / s
            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)


def test_car_fleet():
    sol = Solution()

    # Given examples
    assert sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert sol.carFleet(10, [3], [3]) == 1
    assert sol.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1

    # Basics
    assert sol.carFleet(10, [0], [1]) == 1
    assert sol.carFleet(10, [0, 5], [2, 1]) == 1  # tie at target -> same fleet

    # Rear car arrives later (can't catch) -> two fleets
    assert sol.carFleet(10, [6, 8], [1, 2]) == 2

    # Mixed order & multiple merges
    assert sol.carFleet(10, [8, 3, 7, 4], [2, 4, 1, 3]) == 2

    # Strictly increasing times from front to back -> each car is its own fleet
    # (e.g., equal speeds)
    assert sol.carFleet(20, [15, 10, 5, 0], [1, 1, 1, 1]) == 4

    # Cross-check equivalence with stack method on several cases
    cases = [
        (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]),
        (10, [3], [3]),
        (100, [0, 2, 4], [4, 2, 1]),
        (10, [0, 5], [2, 1]),
        (10, [6, 8], [1, 2]),
        (10, [8, 3, 7, 4], [2, 4, 1, 3]),
        (20, [15, 10, 5, 0], [1, 1, 1, 1]),
    ]
    for tgt, pos, sp in cases:
        assert sol.carFleet(tgt, pos, sp) == sol.carFleet_stack(tgt, pos, sp)

    print("All test cases passed!")


if __name__ == "__main__":
    test_car_fleet()