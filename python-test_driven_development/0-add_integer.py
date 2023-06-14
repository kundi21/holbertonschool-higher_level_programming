#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Test add_integer

    >>> add_integer(1, 98)
    99

    """
    a = 1
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
