# Common Denominators
# https://www.codewars.com/kata/54d7660d2daf68c619000d95/solutions/python?filter=me&sort=best_practice&invalids=false

import math
def convert_fracts(lst):
    if not lst:
        return lst
    cmn_d = lst[0][1]
    for pr in lst[1:]:
        cmn_d *= pr[1]
    mults = []
    for pr in lst:
        mults.append(int(cmn_d / pr[1]))
    lcm = cmn_d
    for mult in mults:
        lcm = math.gcd(lcm, mult)
    cmn_d = int(cmn_d / lcm)
    res = []
    for pr in lst:
        pr_mult = int(cmn_d / pr[1])
        res.append([
            pr[0] * pr_mult,
            pr[1] * pr_mult
        ])
    return res
