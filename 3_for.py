"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
 [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
data = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
def main(data):
    all_sales = 0
    all_products = len(data)
    for phone in data:
        product = phone['product']
        sales = phone['items_sold']
        total_sales = sum(sales)
        avg_sales = round(total_sales / len(sales), 2)

        print(f'телефон: {product} суммарное колиичество продаж: {total_sales}, среднее количество продаж: {avg_sales}')

        all_sales += total_sales
    
    avg_all_sales = round(all_sales / all_products, 2)
    print(f'суммарное количество продаж {all_sales}')
    print(f'среднее количество продаж {avg_all_sales}')
    
main(data)

input()
  
    #"""
    #Эта функция вызывается автоматически при запуске скрипта в консоли
    #В ней надо заменить pass на ваш код
    #"""
    #pass
    
#if __name__ == "__main__":
   #main()
