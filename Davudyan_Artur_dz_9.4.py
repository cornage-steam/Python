class Car:

    def __init__(self, speed, color, name, is_police):  # не понимаю, почему "не используется"
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True or False

    def go(self):
        if self.is_police:
            print(f'{self.name} выдвигается на вызов')
        else:
            print(f'{self.name} начинает движение')

    def stop(self):
        if self.is_police:
            print(f'{self.name} прибыла к месту преступления')
        else:
            print(f'{self.name} останавливается')

    def turn(self, direction):
        if self.is_police:
            print(f'{self.name} совершает оперативный поворот {direction}')
        else:
            print(f'{self.name} повернул {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} = {self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости на {self.speed - 60} км/ч!')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости на {self.speed - 40} км/ч!')


class PoliceCar(Car):
    pass

police = PoliceCar(100, 'Белый', 'Полицейский автомобиль', True)
police.go()
police.turn('направо')
police.show_speed()
town_car = TownCar(70, 'Черный', 'Городской автомобиль', False)
town_car.show_speed()