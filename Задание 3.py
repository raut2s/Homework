class Cell:
    def __init__(self, cell):
        self.cell = cell
        self.designation = '*'

    def __str__(self):
        return str(f'Количество ячеек - {self.cell}')

    def __sub__(self, other):
        return Cell(abs(self.cell - other.cell))

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def __add__(self, other):
        return Cell(abs(self.cell + other.cell))

    def make_order(self, count):
        x = self.cell
        while x > 0:
            for k in range(1,count+1):
                print(self.designation, end='')
                x -= 1
                if x <= 0:
                    break
            print('\n', end = '')



a = Cell(4)
b = Cell(5)
c = Cell(7)
d = Cell(1)

print(a + b)
print(a - b)
print(a * b)
print(c / d)

a.make_order(4)
b.make_order(2)