# class Solution(object):
def lengthOfLastWord(s):
    lst = s.split(" ")
    for i in range(len(lst) -1, -1, -1):
        if lst[i] == "":
            lst.remove(lst[i])
    return len(lst[len(lst)-1])
