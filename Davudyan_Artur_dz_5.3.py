tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Андрей']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б']

def gen(a, b):
    _a = (el for el in a)
    _b = (el for el in b)
    for data in zip(_b, _a):
        yield data[::-1]
    for result in _a:
        yield result, None

for i in gen(tutors, klasses):
    print(i)