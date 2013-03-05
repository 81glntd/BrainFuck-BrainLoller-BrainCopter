if __name__ == "__main__":
    bCode = input()
    if len(bCode) == 0: print("nic si nezadal tupce")
    array = [0] * 30000
    i = 0
    pointer = 0
    for x in range(0, len(bCode)):
        if bCode[x] == '>': #move pointer to left
            pointer += 1
            if pointer >= len(bCode):
                print(
                    "Wrong format of Brainfuck code!! Last char int your code is to move to next cell, but there is no reason to do that, cause this is last piece of code!! Keep the code clean")
        elif bCode[x] == '<': #move pointer to rigth
            pointer -= 1
            if i >= len(bCode):
                print(
                    "Wrong format of Brainfuck code!! Last char int your code is to move to previous cell, but there is no reason to do that, cause this is last piece of code!! Keep the code clean")
        elif bCode[x] == '+': #increment of the actual cell
            array[pointer] += 1
        elif bCode[x] == '-': #decrement of the actual cell
            array[pointer] -= 1
        elif bCode[x] == '.': #actual printing of the actual cell value
            print(chr(array[pointer], end=""))
        elif bCode[x] == ',':
            if idx >= 0 and idx < len(data):
                array[pointer] = ord(data[idx])
                idx += 1
        elif bCode[x] == '[':
            if array[pointer] == 0:
                cycle = 1
                while cycle > 0:
                    x += 1
                    c = bCode[x]
                    if c == '[':
                        cycle += 1
                    elif c == ']':
                        cycle -= 1
        elif bCode[x] == ']':
            cycle = 1
            while cycle > 0:
                i -= 1
                c = bCode[x]
                if c == '[':
                    cycle -= 1
                elif c == ']':
                    cycle += 1
            x -= 1
        x += 1




