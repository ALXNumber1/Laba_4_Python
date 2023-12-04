import math


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_triangle(self):

        if self.side1 + self.side2 > self.side3 and \
            self.side1 + self.side3 > self.side2 and \
            self.side2 + self.side3 > self.side1:
            return True
        else:
            return False

    def calculate_area(self):

        if self.is_triangle:
            s = (self.side1 + self.side2 + self.side3) / 2
            area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
            return area
        else:
            return "Треугольника не существует"

    def calculate_perimeter(self):

        if self.is_triangle():
            perimeter = self.side1 + self.side2 + self.side3
            return perimeter
        else:
            return "Треугольника не существует"

triangle1 = Triangle(3, 4, 5)

if triangle1.is_triangle():
    print("Площадь треугольника:", triangle1.calculate_area())
    print("Периметр треугольника:", triangle1.calculate_perimeter())
else:
    print("Треугольника не существует")