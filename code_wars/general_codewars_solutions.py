# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

# 1st TAKE

def domain_name(url):
    lst = url.split("/")

    str_core = ""
    for s in lst:
        if not (s == "http:" or s == "https:" or s == ""):
            str_core += s
            break

    str_core = str_core.split(".")

    if str_core[0] == "www":
        return str_core[1]
    else:
        return str_core[0]

"""
First run through, this is done in linear time, iterations will never pass the first 3 items of the input.
"""

# Alternate Regex Solution:
# docs: https://docs.python.org/3/library/re.html?highlight=re#module-re

import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')


# Mean Square Error
# https://www.codewars.com/kata/51edd51599a189fe7f000015/train/python

def solution(array_a, array_b):
    return sum(
            [(array_a[i] - array_b[i]) ** 2 for i in range(len(array_a))]
        ) / len(array_a)

def solution(a, b):
    return sum((x - y)**2 for x, y in zip(a, b)) / len(a)



# Last digit of a large number
# https://www.codewars.com/kata/5511b2f550906349a70004e1/python

def last_digit(n1, n2):
    return pow( n1, n2, 10 )

digits = {
    0:[0,0,0,0],
    1:[1,1,1,1],
    2:[2,4,8,6],
    3:[3,9,7,1],
    4:[4,6,4,6],
    5:[5,5,5,5],
    6:[6,6,6,6],
    7:[7,9,3,1],
    8:[8,4,2,6],
    9:[9,1,9,1]
}
def last_digit(n1, n2):
    return digits[n1%10][(n2-1)%4] if n2 else 1
