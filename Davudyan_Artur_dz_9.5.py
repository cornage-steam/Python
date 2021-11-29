class Stationery:

    def __init__(self, tittle):
        self.tittle = tittle

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print(f'{self.tittle} нужна чтобы писать')


class Pencil(Stationery):

    def draw(self):
        print(f'{self.tittle} нужен чтобы чертить')


class Handle(Stationery):

    def draw(self):
        print(f'{self.tittle} нужен чтобы рисовать')


pen = Pen('Ручка')
pen.draw()
pensil = Pencil('Карандаш')
pensil.draw()
handle = Handle('Маркер')
handle.draw()


# Проверка
class Ruler(Stationery):
    pass


ruler = Ruler('Линейка')
ruler.draw()