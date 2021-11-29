class Worker:

    def __init__(self, name, surname, position, **income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя сотрудника: {str.capitalize(self.surname)} {str.capitalize(self.name)}')

    def get_total_income(self):
        print(f'Доход сотрудника с учетом премии {self._income.get("wage") * self._income.get("bonus")}')


worker_1 = Position('Артур', 'Давудян', 'Программист', wage=20000, bonus=20000)
worker_1.get_full_name()


# Или

# class Worker:
#
#     def __init__(self, name, surname, position, income):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = income
#
#
# class Position(Worker):
#
#     def get_full_name(self):
#         print(f'Полное имя сотрудника: {str.capitalize(self.surname)} {str.capitalize(self.name)}')
#
#     def get_total_income(self):
#         print(f'Доход сотрудника с учетом премии {self._income.get("wage") + self._income.get("bonus")}')
#
# income = {'wage': 20000, 'bonus': 20000}
#
# worker_1 = Position('Артур', 'Давудян', 'Программист', income)
# worker_1.get_full_name()
# worker_1.get_total_income()
