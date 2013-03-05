# coding UTF-8
__author__ = 'Tomas Sykora'


def MyInput():
    """
    Just simple function for getting the bf code into var.
    """
    source = input()
    return source


def Harakiri():
    print("Sorry, something went wrong probably your fault!")


def Handle(source):
    p_ToSource = 0
    p_ToArray = 0
    bfArray = [0] * 30000
    i = 0
    if len(source) == 0:
        Harakiri()
    for i in len(source):
        if source[p_ToSource] == '+':
            bfArray[p_ToArray] += 1
        elif source[p_ToSource] == '-':
            bfArray[p_ToArray] -= 1
        elif source[p_ToSource] == '>':
            p_ToArray += 1
        elif source[p_ToSource] == '<':
            p_ToArray -= 1
        elif source[p_ToSource] == '.':
            print(chr(bfArray[p_ToArray]))


if __name__ == "__main__":
    Handle(MyInput())

