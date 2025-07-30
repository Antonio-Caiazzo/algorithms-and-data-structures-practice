# LeetCode 933 - Number of Recent Calls (Easy)
#
# You have a RecentCounter class that counts the number of recent requests within a 3000ms time window.
#
# Implement the RecentCounter class:
# - RecentCounter() initializes the counter.
# - int ping(int t) adds a new request at time t (in milliseconds), and returns the number of requests in the past 3000ms.
# 
# The range is inclusive: [t - 3000, t].
# All pings are strictly increasing in t.
#
# Example:
# Input:
# ["RecentCounter","ping","ping","ping","ping"]
# [[],[1],[100],[3001],[3002]]
#
# Output:
# [null,1,2,3,3]
#
# Explanation:
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // returns 1
# recentCounter.ping(100);   // returns 2
# recentCounter.ping(3001);  // returns 3
# recentCounter.ping(3002);  // returns 3
#
# Time complexity: O(1) amortized per operation, but in worst case is O(n)
# Space complexity: O(n), where n is number of pings stored in the 3000ms window

from collections import deque

class RecentCounter:
    def __init__(self):
        self.count = deque()

    def ping(self, t: int) -> int:
        self.count.append(t)
        while self.count[0] < t - 3000:
            self.count.popleft()
        return len(self.count)


# Test cases for RecentCounter
def test_recent_counter():
    print("Running test cases for RecentCounter...")
    rc = RecentCounter()
    assert rc.ping(1) == 1, "Expected 1"
    assert rc.ping(100) == 2, "Expected 2"
    assert rc.ping(3001) == 3, "Expected 3"
    assert rc.ping(3002) == 3, "Expected 3"
    print("All test cases passed!")


if __name__ == "__main__":
    test_recent_counter()
