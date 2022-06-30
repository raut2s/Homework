class Worker:    
    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.bonus = bonus

class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)
    def get_full_name(self):
        return self.name + ' ' + self.surname
    def get_full_profit(self):
        self._income = {'profit': self.profit, 'bonus': self.bonus}
        return self._income

manager = Position('Pavel', 'Lonchinskiy', 'doctor', 500000, 1000000)
print(manager.get_full_name(), manager.get_full_profit())
print(manager.name)
print(manager.surname)
print(manager.position)
