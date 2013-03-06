import math


def t1():
    for number in range(2, 101):
        if number % 3 == 0 or number % 5 == 0:
            print(number)


def primes():
    print("\nPrimes:")
    for n in range(2, 101):
        for x in range(2, int(math.sqrt(n)) + 1):
            if n % x == 0:
                break
        else:
            print(n, end=' ')


def echo(filename):
    print("\n\nVypis ze souboru file.txt")
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end=' ')




if __name__ == "__main__":
    t1()
    primes()
    echo('file.txt')
