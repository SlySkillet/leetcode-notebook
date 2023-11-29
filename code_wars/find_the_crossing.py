def find_the_crossing(a, b, c, d):
    m1 = (b[1] - a[1]) / (b[0] - a[0])
    m2 = (d[1] - c[1]) / (d[0] - c[0])
    if m1 == m2:
        return None
    x = (m1 * b[0] - b[1] - m2 * d[0] + d[1]) / (m1 - m2)
    y = m1 * (x - a[0]) + a[1]
    res = (x, y)
    return res
