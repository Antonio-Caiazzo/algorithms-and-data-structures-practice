# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you caannot use additional data structures?

# Time complexity: O(n)
# Space complexity: O(n)
def is_unique(s: str) -> bool:
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True
print(is_unique("hello"))       # False
print(is_unique("world"))       # True



# Time complexity: O(n^2)
# Space complexity: O(1)
def is_unique(s: str) -> bool:
    n=len(s)
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                return False
    return True
print(is_unique("hello"))       # False
print(is_unique("world"))       # True



# Time complexity: O(n log n)
# Space complexity: O(n)
def is_unique(s: str) -> bool:
    s = sorted(s)
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            return False
    return True
print(is_unique("hello"))       # False
print(is_unique("world"))       # True