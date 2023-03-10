"o][o]gg"
def zad0():

    words = []
    while (new_word := str(input())) != "stop":
            words.append(new_word)
    print(" ".join(words))


def zad2():

    words = []
    while (new_word := str(input())) != "stop":
        if "ф" in new_word or "Ф" in new_word:
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово...")

def zad3():

    from random import randint
    p = 0
    k = 0
    print("Для завершения игры введите слово stop")
    while True:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f"{a} + {b} = ", end="")
        res = input()

        while not res.isdigit() and res != "stop":
            print("Вы ввели что-то не то, повторите ввод: ", end="")
            res = input()
        if res == "stop":
            break
        res = int(res)
        if a + b == res:
            k += 1
            print("Правильно")
        else:
            print("Ответ неверный")
            p += 1
        if p >= 3:
            print("Игра окончена. Правильных ответов =", k)




zad0()
