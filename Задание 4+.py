class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return('Машина поехала')

    def stop(self):
        return('Машина остановилась')

    def turn_right(self):
        return('Машина повернула направо')
        
    def turn_left(self):
        return('Машина повернула налево')

    def show_speed(self):
            print("Машина двигается с нормальной скоростью")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
            super().__init__(speed, color, name, is_police)
    
    def show_speed(self):
        if self.speed > 60:
            return "Машина двигается с превышением скорости"
        else:
            return "Машина двигается с нормальной скоростью"

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    
    def show_speed(self):
        if self.speed > 40:
            return "Машина двигается с превышением скорости"
        else:
            return "Машина двигается с нормальной скоростью"

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


lamborghini_aventador = SportCar(300, 'Black', 'Lamborghini Aventador', False)
skoda_octavia = TownCar(50, 'Blue', 'Skoda Octavia', True)
suzuki_grand_vitara = WorkCar(70, 'Rose', 'Suzuki Grand Vitara', False)
lada_granta = PoliceCar(30, 'White_Blue', 'Lada Granta', True)

print(lamborghini_aventador.name, lamborghini_aventador.color, lamborghini_aventador.speed, lamborghini_aventador.is_police)
print(suzuki_grand_vitara.turn_left())
print(lada_granta.turn_right())
print(skoda_octavia.stop())
print(lamborghini_aventador.go())
print(lada_granta.is_police)
print(lamborghini_aventador.is_police)
print(suzuki_grand_vitara.show_speed())
print(skoda_octavia.show_speed())
