# LeetCode 735 - Asteroid Collision (Medium)
#
# We are given an array asteroids of integers representing asteroids in a row.
# - The absolute value represents its size
# - The sign represents its direction:
#     * positive -> moving right
#     * negative -> moving left
# All asteroids move at the same speed.
#
# Rules:
# - If two asteroids meet, the smaller one explodes
# - If they are the same size, both explode
# - Two asteroids moving in the same direction never meet
#
# Example 1:
# Input:  asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide, resulting in 10. The 5 and 10 never collide.
#
# Example 2:
# Input:  asteroids = [8,-8]
# Output: []
# Explanation: Both explode since they have the same size.
#
# Example 3:
# Input:  asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide → -5 survives. Then 10 and -5 collide → 10 survives.
#
# Constraints:
# - 2 <= asteroids.length <= 10^4
# - -1000 <= asteroids[i] <= 1000
# - asteroids[i] != 0
#
# Time complexity: O(n) 
# Space complexity: O(n) 

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                diff = stack[-1] + asteroid
                if diff > 0:       
                    asteroid = 0
                elif diff == 0:    
                    stack.pop()
                    asteroid = 0
                else:              
                    stack.pop()
            if asteroid:
                stack.append(asteroid)
        return stack


# Test cases for Asteroid Collision
def test_asteroid_collision():
    print("Running test cases for Asteroid Collision...")
    sol = Solution()

    assert sol.asteroidCollision([5,10,-5]) == [5,10], "Test 1 failed"
    assert sol.asteroidCollision([8,-8]) == [], "Test 2 failed"
    assert sol.asteroidCollision([10,2,-5]) == [10], "Test 3 failed"

    # Extra cases
    assert sol.asteroidCollision([-2,-1,1,2]) == [-2,-1,1,2], "Test 4 failed"
    assert sol.asteroidCollision([1,-2,-2,-2]) == [-2,-2,-2], "Test 5 failed"
    assert sol.asteroidCollision([1,2,3,-3,-2,-1]) == [], "Test 6 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_asteroid_collision()
