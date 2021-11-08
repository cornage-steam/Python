import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(arg):
    new_list = []
    result = []
    count = 0
    while count < arg:
        new_list.append(random.choice(nouns))   # добавляем случайной элемент из списка
        new_list.append(random.choice(adverbs))  # -//-
        new_list.append(random.choice(adjectives))  # -//-
        result.append(' '.join(new_list))  # добавляем в результирующий список случайные элементы, разделенные пробелом
        new_list.clear() # очищаем список со случайными элементами
        count += 1
    print(result)

get_jokes(5)
