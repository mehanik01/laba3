"""
words = []
while (new_word := str(input())) != "stop":
    words.append(new_word)

print(" ".join(words))
"""

"""
words = []
while (new_word := str(input())) != "stop":
    if "ф" in new_word or "Ф" in new_word:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")
"""

from random import randint

print("Для завершения игры введите слово stop")
while True:
    a = randint(1, 100)
    b = randint(1, 100)
    print(f"{a} + {b} = ", end="")
    res = input()
    # проверка ввода
    while not res.isdigit() and res != "stop":
        print("Вы ввели что-то не то, повторите ввод: ", end="")
        res = input()
    if res == "stop":
        break
    res = int(res)
    if a+b == res:
        print("Правильно!")
    else:
        print("Ответ неправильный :(")
