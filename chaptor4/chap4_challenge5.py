def string_to_float(x):
    """
    Converts passed in str to int.
    :param x: str.
    :return: string converted to int.
    """
    try:
        return float(x)
    except ValueError:
        print("It can not convert 'string' to 'float'.")

y = string_to_float("aaa")
print(y)