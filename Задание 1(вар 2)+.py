from time import sleep

class TrafficLight:
    def __init__(self):
        self.__color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается\n 'f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1

TrafficLight = TrafficLight()
TrafficLight.running()