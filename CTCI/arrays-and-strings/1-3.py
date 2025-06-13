# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# Time complexity: O(n)
# Space complexity: O(n)
def URLify(s: str, lenght: int) -> str:
    result = []
    for i in range(lenght):
        if s[i] == " ":
            result.extend(["%", "2", "0"])
        else:
            result.append(s[i])
    return "".join(result)
print(URLify("Mr John Smith", 13))       # Mr%20John%20Smith
