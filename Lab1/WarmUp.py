__author__ = 'syky'
import sys


def Count(x, y, z):
    """
    Sectete cisla 3, 4 a 5.
    """
    print(x + y + z)


def PowCount(x, y, z):
    print(pow(x, 2) + pow(y, 2) + pow(z, 2))


def Pythagoras(x, y, z):
    max = x
    if max < y:
        max = y
    if max < z:
        max = z
    if max == x & (pow(z, 2) + pow(y, 2) == pow(x, 2)):
        print("Pythagorova veta plati")
    if 0 == (max == z & (pow(x, 2) + pow(y, 2) == pow(z, 2))):
        print("Pythagorova veta plati")
    if max == y & (pow(x, 2) + pow(z, 2) == pow(y, 2)):
        print("Pythagorova veta plati")


def FitInReal(x, y):
    return y / x


def FitInInt(x, y):
    return y // x


def Modulo(x, y):
    return y % x


if __name__ == "__main__":
    Count(3, 4, 5)
    PowCount(3, 4, 5)
    Pythagoras(3, 4, 5)
    print(FitInReal(7, 51))
    print(FitInInt(7, 51))
    print(Modulo(7, 51))
