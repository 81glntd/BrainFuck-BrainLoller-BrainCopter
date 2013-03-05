def task1():
    text = "Ahoj, světe!"
    for char in text:
        if char.isalpha():
            if char.lower() in "aáeéěiíouúů":
                print(char, "Samohláska")
            else:
                print(char, "Souhláska")
        else:
            print(char)


def task2():
    text = "Ahoj! Jak se máš?"
    print(text)
    print(text[:len(text) // 2])


def task3(Text_task3):
    print(Text_task3)
    print(task3_Half(Text_task3))

def task3_Half(Text_Half_task3):
   return Text_task3[:len(Text_task3) // 2]


def task4(Text_task4):
    if "m" in Text_task4:
        print(Text_task4[:Text_task4.index("m")])
    else:
        print(Text_task4)


def task5(t):
    counter = 0
    for c in t:
        if c == "a" or c == "A" or c == "á":
            counter += 1
    return counter


if __name__ == "__main__":
    task1()
    task2()
    Text_task3 = "Ahoj! Jak se máš?"
    task3(Text_task3)
    Text_task4 = "Ahoj! Jak se máš?"
    task4(Text_task4)
    t = "Ahoj! Jak se máš?"
    print(task5(t))