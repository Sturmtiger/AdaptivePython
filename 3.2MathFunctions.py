def f(x):
    return ((x <= -2) * (1 - (x + 2) ** 2)
            or (-2 < x <= 2) * -(x/2)
            or (2 < x) * ((x - 2) ** 2 + 1))
