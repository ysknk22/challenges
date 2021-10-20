def f(a, b, c, d=10, e=25):
    """
    Returns a * b / c + d + e
    :param a: int.
    :param b: int.
    :param c: int.
    :param d: int.
    :param e: int.
    :return: int.
    """
    return a * b / c + d + e

print(f(100, 20, 2))