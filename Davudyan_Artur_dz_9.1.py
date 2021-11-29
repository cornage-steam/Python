import sys
import os
from time import sleep


class TrafficLight:

    def __init__(self):
        self.color = ['Красный', 'Жёлтый', 'Зелёный']

    def running(self):
        while True:
            print(f'\033[31m{self.color[0]}')
            sleep(7)
            os.system(
                'clear')  # у меня почему-то работает только с эмуляцией терминала (Run/Edit Configurations/emulate
            # terminal in output console)
            print(f'\033[33m{self.color[1]}')
            sleep(2)
            os.system('clear')
            print(f'\033[32m{self.color[2]}')
            sleep(3)
            os.system('clear')
            sys.exit(1)  # выход из программы


traffic_light = TrafficLight()
traffic_light.running()
