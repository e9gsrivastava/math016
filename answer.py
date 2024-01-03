"""this is to find 2**n where n is a very large no """
from solver import solver


def answer():
    """this func calls generic func to get the value of 2**100"""

    return solver(1000)


if __name__ == "__main__":
    print(answer())
