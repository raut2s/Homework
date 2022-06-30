class Road:
    _length = None
    _width = None
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def mass(self):
        self.weigth = 25
        self.thickness = 0.05
        mass = self.length * self.width * self.weigth * self.thickness / 1000
        print(f'Необходимо {mass} тонн асфальта для покрытия дороги')

road_to_village = Road(20000, 6)
road_to_village.mass()
