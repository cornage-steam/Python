class Matrix:

    def __init__(self, data):
        self.data = data
        for line in self.data[:-1]:
            if not len(line) == len(self.data[self.data.index(line) + 1]):
                raise ValueError('Количество элементов в строках не совпадает')

    def __str__(self):
        return '\n'.join('\t'.join(str(num) for num in line) for line in self.data)

    def __add__(self, other):
        if not len(self.data) == len(other.data):
            raise ValueError('Размерности матриц не совпадают')
        else:
            for i in range(len(self.data)):
                if not len(self.data[i]) == len(other.data[i]):
                    raise ValueError('Размерности матриц не совпадают')
            item = [[int(self.data[line][num]) + int(other.data[line][num]) for num in
                     range(len(self.data[line]))] for line in range(len(self.data))]
            return Matrix(item)


a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
b = [[12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
c = [[1, 2, 3, 4], [5, 6, 7, 8]]  # проверка
matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
matrix_3 = Matrix(c)

print(f'Matrix 1 + Matrix 2\n{matrix_1 + matrix_2}')
print(f'Matrix 2 + Matrix 3\n{matrix_2 + matrix_3}')
