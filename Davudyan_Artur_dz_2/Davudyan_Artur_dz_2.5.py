lst = [867.1, 6549.21, 54651.55, 36584.25, 123, 21.07, 2589.24, 148.02, 1428.36, 257, 126843.21]
print('Исходный список: ', lst)


def is_price(x):
    pricelst = []
    for item in x:
        rub = int(item)
        kop = int(item % 1 * 100)
        if kop == 0:
            kop = '00'
        price = f'{rub} руб {kop} коп'
        pricelst.append(price)
    return pricelst

print('Цены через запятую в одну строку: ', ', '.join(is_price(lst)))
print('Цены, отсортированные по возрастанию, без создания нового списка: ', ', '.join(is_price(sorted(lst))))
print('Проверка: ', lst)
lst2 = sorted(lst, reverse=True)
print('Цены пяти самых дорогих товаров: ', ', '.join(is_price(lst2[:5])))
