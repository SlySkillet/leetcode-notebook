# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/description/
# class Solution(object):
def lengthOfLastWord(s):
        # """
        # :type s: str
        # :rtype: int
        # """
    lst = s.split()
    print(lst)
    return len(lst[len(lst)-1])

print(lengthOfLastWord("hello     world    sup?"))
