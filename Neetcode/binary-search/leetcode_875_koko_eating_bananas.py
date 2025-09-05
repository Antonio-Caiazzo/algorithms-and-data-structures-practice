# LeetCode 875 - Koko Eating Bananas (Medium)
#
# Koko loves to eat bananas. There are `n` piles of bananas, where the i-th pile has piles[i] bananas.
# The guards will return in `h` hours. Each hour, Koko eats bananas at a fixed speed `k` (bananas/hour).
# In each hour, she chooses one pile and eats up to `k` bananas. If the pile has fewer than `k` bananas,
# she eats all of them and will not eat more in that hour.
#
# Return the minimum integer `k` such that she can finish all the bananas within `h` hours.
#
# Examples:
# Input:  piles = [3,6,7,11], h = 8
# Output: 4
#
# Input:  piles = [30,11,23,4,20], h = 5
# Output: 30
#
# Input:  piles = [30,11,23,4,20], h = 6
# Output: 23
#
# Constraints:
# - 1 <= piles.length <= 10^4
# - piles.length <= h <= 10^9
# - 1 <= piles[i] <= 10^9
#
# Approach:
# - We use binary search on Koko's eating speed `k`.
# - Lower bound = 1 (minimum possible speed).
# - Upper bound = max(piles) (if Koko eats an entire pile per hour).
# - For each mid, simulate total hours required.
#   - If total_hours > h, speed is too small → move right.
#   - Otherwise, speed is sufficient → move left, try smaller k.
#
# Time complexity: O(n * log(max(piles)))
# Space complexity: O(1)

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = (l + r) // 2
            total = 0
            for p in piles:
                total += (p + mid - 1) // mid
            if total > h:  
                l = mid + 1
            else:          
                res = mid
                r = mid - 1

        return res


# -----------------------------
# Test cases for Koko Eating Bananas
# -----------------------------
def test_min_eating_speed():
    print("Running test cases for Koko Eating Bananas...")
    sol = Solution()

    assert sol.minEatingSpeed([3,6,7,11], 8) == 4, "Test 1 failed"
    assert sol.minEatingSpeed([30,11,23,4,20], 5) == 30, "Test 2 failed"
    assert sol.minEatingSpeed([30,11,23,4,20], 6) == 23, "Test 3 failed"

    # Extra cases
    assert sol.minEatingSpeed([5], 5) == 1, "Test 4 failed"           # 1 banana/hour
    assert sol.minEatingSpeed([5], 1) == 5, "Test 5 failed"           # must eat all in 1 hour
    assert sol.minEatingSpeed([1,1,1,1], 4) == 1, "Test 6 failed"     # multiple piles
    assert sol.minEatingSpeed([9,8,7,6,5], 5) == 9, "Test 7 failed"   # one per hour

    print("All test cases passed!")


if __name__ == "__main__":
    test_min_eating_speed()
