# LeetCode 1011 - Capacity To Ship Packages Within D Days (Medium)
#
# A conveyor belt has packages that must be shipped from one port to another within `days` days.
# Each day, we load the ship with packages in the given order (no reordering),
# without exceeding the ship's maximum capacity.
#
# Return the minimum ship capacity needed to deliver all packages within the given `days`.
#
# Examples:
# Input:  weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
#
# Input:  weights = [3,2,2,4,1,4], days = 3
# Output: 6
#
# Input:  weights = [1,2,3,1,1], days = 4
# Output: 3
#
# Constraints:
# - 1 <= days <= weights.length <= 5 * 10^4
# - 1 <= weights[i] <= 500
#
# Approach:
# - Binary search sulla capacità minima C.
#   - Lower bound = max(weights) (almeno il pacco più pesante).
#   - Upper bound = sum(weights) (tutti i pacchi in un giorno).
# - Ad ogni tentativo, verifichiamo se la capacità è sufficiente simulando la spedizione.
#
# Time complexity: O(n * log(sum(weights))), where n = len(weights)
# Space complexity: O(1)

from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity: int) -> bool:
            day = 1
            current_capacity = 0
            for weight in weights:
                if weight + current_capacity > capacity:
                    day += 1
                    current_capacity = 0
                current_capacity += weight
                if day > days:
                    return False
            return True

        l, r = max(weights), sum(weights)
        while l < r:
            mid = l + (r - l) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l


# -----------------------------
# Test cases for Capacity To Ship Packages Within D Days
# -----------------------------
def test_ship_within_days():
    print("Running test cases for Capacity To Ship Packages Within D Days...")
    sol = Solution()

    assert sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5) == 15, "Test 1 failed"
    assert sol.shipWithinDays([3,2,2,4,1,4], 3) == 6, "Test 2 failed"
    assert sol.shipWithinDays([1,2,3,1,1], 4) == 3, "Test 3 failed"
    assert sol.shipWithinDays([5], 1) == 5, "Test 4 failed"
    assert sol.shipWithinDays([10,10,10], 3) == 10, "Test 5 failed"
    assert sol.shipWithinDays([10,10,10], 1) == 30, "Test 6 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_ship_within_days()
