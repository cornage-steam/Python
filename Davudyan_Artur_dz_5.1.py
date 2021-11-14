def gen(n):
    for el in range(0, n + 1):
        if el % 2 != 0:
            yield el

result = gen(5)
print(next(result))
print(next(result))
print(next(result))
# print(next(result))  # истощение генератора

# Вариант без использования yield

gen_adv = int(input('Введите число: ')) # 5 для примера
result_adv = (el for el in range(0, gen_adv + 1) if el % 2 != 0)

print(next(result_adv))
print(next(result_adv))
print(next(result_adv))
# print(next(result_adv)) # истощение генератора (если gen_adv(5))







