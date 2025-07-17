# LeetCode 88 - Merge Sorted Array (Easy)
#
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums2 into nums1 as one sorted array in-place.
# nums1 has length m + n, with the first m elements initialized, and the rest set to 0.
#
# Do the merge in-place with O(1) extra space.
#
# Example 1:
# Input:  nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
#
# Example 2:
# Input:  nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
#
# Example 3:
# Input:  nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
#
# Constraints:
# - nums1.length == m + n
# - nums2.length == n
# - 0 <= m, n <= 200
# - 1 <= m + n <= 200
# - -10^9 <= nums1[i], nums2[j] <= 10^9
#
# Time complexity: O(m + n)
# Space complexity: O(1)
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k = n + m -1

        while  m > 0 and n > 0:
            if nums2[n - 1] >= nums1[m - 1]:
                nums1[k] = nums2[n - 1]
                n -= 1
            else:
                nums1[k] = nums1[m - 1]
                m -= 1
            k -= 1  
        
        while n > 0:
            nums1[k] = nums2[n - 1]
            k, n = k - 1, n - 1
        

# Test 
def test_merge():
    s = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    s.merge(nums1, 3, [2, 5, 6], 3)
    print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

    nums2 = [1]
    s.merge(nums2, 1, [], 0)
    print(nums2)  # Output: [1]

    nums3 = [0]
    s.merge(nums3, 0, [1], 1)
    print(nums3)  # Output: [1]

    nums4 = [2, 0]
    s.merge(nums4, 1, [1], 1)
    print(nums4)  # Output: [1, 2]

test_merge()
