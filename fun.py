def add2num(a, b=1):
    """
    :param a: to be supplied
    :param b: optional, default 1
    :return: parameter c sum of a and b if b not supplied will take as 1 default
    """
    c = a + b
    return c


x = add2num(2, 4)
print("sum = ", x)
