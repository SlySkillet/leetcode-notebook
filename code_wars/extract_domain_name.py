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

import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
