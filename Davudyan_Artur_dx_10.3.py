class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, row_len):
        result = ['*' * row_len * (self.nums // row_len)]
        if self.nums % row_len:
            result.append('*' * row_len * (self.nums % row_len))
        return '\n'.join(result)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        print('Сумма клеток: ')
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print('Вычитание клеток: ')
        if self.nums < other.nums:
            raise ValueError('Вычитание невозможно!')
        return Cell(self.nums - other.nums)

    def __mul__(self, other):
        print('Умножение клеток: ')
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print('Деление клеток: ')
        return Cell(self.nums // other.nums)

cell_1 = Cell(15)
cell_2 = Cell(24)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(7))