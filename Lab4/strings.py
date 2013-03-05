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


def task4_modified(text):
    print("\ntask4_modified")
    if "m" in text:
        return text[:text.index("m")]
    else:
        return text


def task5(t):
    counter = 0
    for c in t:
        if c == "a" or c == "A" or c == "á":
            counter += 1
    return counter


def test():
    text = "123456789"
    for letter in text:
        if letter == "4":
            print(text[:text.index("4")])
            print(text[:4])


def task5_modified(text, x):
    print("\nTask 5 heavily modied", text.count(x))



if __name__ == "__main__":
    task1()
    task2()
    Text_task3 = "Ahoj! Jak se máš?"
    task3(Text_task3)
    Text_task4 = "Ahoj! Jak se máš?"
    task4(Text_task4)
    t = "Ahoj! Jak se máš?"
    print(task5(t))
    text = "Jak jsi na tom, co dnes podniknem?"
    print(task4_modified(text))
    test()
    task5_modified(text, 'a')