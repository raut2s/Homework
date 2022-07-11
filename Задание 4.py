class Office_equipment:
    def __init__(self, title, serial_number):
        self.title = title
        self.serial_number = serial_number

    def __str__(self):
        return str(self.title)

class Printer(Office_equipment):
    def __init__(self,title,serial_number, print_velocity):
        Office_equipment.__init__(self,title, serial_number)
        self.print_velocity = print_velocity

    def __str__(self):
        return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.print_velocity)


class Scanner(Office_equipment):
    def __init__(self, title,serial_number,resolution):
        Office_equipment.__init__(self,title, serial_number)
        self.resolution = resolution

    def __str__(self):
        return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.resolution)

class Copier(Office_equipment):
    def __init__(self, title,serial_number, addit):
        Office_equipment.__init__(self, title, serial_number)
        self.addit = addit

    def __str__(self):
        return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.addit)



a = Printer('HP', 345678, 100)
b = Scanner('Epson', 123456, 4000)
c = Copier('Brother',987654, 50)
d = Printer('HP',245678,200)

print(a)
print(b)
print(c)
print(d)