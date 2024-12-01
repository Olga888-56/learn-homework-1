"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
#    """
#   Замените pass на ваш код
#   """
    while True:
        how_are_you = input('Как дела? ')
        if how_are_you == ('хорошо'):
            break
        else:
            print('Как дела? ')
hello_user()

input()
#if __name__ == "__main__":
#    hello_user()
