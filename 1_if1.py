"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def get_activity(age):
    if age >= 2 and age < 7:
           return "Детский сад"
    elif age >=7 and age < 18:
           return "Школа"
    elif age >=18 and age < 23:
           return "вуз"
    elif age >=23 and age < 60:
           return "Работа"
    else:
           return "Старый или малый)"

age_in =  input("Введите ваш возраст: ")
age = int(age_in)
activity = get_activity(age)
print(f"Ваше занятие по возрасту {activity}")    
input ()
"""
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
   # pass

#if __name__ == "__main__":
 #   main()
