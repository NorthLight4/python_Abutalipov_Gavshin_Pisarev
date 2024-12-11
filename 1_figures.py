"""
2.3 Фигуры на плоскости

Принцип подстановки Барбары Лисков: если для любого объекта o1 типа S существует такой объект o2 типа T, что для всех
программ P, определённых в терминах Т, поведение Р не изменяется при подстановке o1 вместо o2, то S - подтип Т.

Проблема исходного кода: код, использующий атрибуты width и height класса Rectangle независимым образом, может работать
некорректно для экземпляров класса Square, нарушая ограничение на равенство сторон

Исправим код при помощи свойств:
"""


class Shape:
    """Геометрические фигуры"""
    name = 'геометрическая фигура'

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return f"{self.name} по координатам ({self.__x}, {self.__y})"


class Rectangle(Shape):
    """Прямоугольники"""
    name = 'прямоугольник'

    def __init__(self, width, height, x=0, y=0):
        super().__init__(x, y)
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return (f"{Shape.__repr__(self)}, со сторонами {self.width} и {self.height},"
                f" с площадью {self.area()} и периметром {self.perimeter()}")


class Square(Rectangle):
    """Квадраты"""
    name = 'квадрат'

    def __init__(self, side, x=0, y=0):
        super().__init__(side, side, x, y)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = self._height = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = self._width = value

    def __repr__(self):
        return (f"{Shape.__repr__(self)}, со стороной {self.width},"
                f" с площадью {self.area()} и периметром {self.perimeter()}")


def main():
    figures = [Rectangle(2, 3), Square(2, 1, 1)]
    for figure in figures:
        print(f'До изменения: {figure}')
        figure.width = 5
        print(f'После изменения ширины: {figure} ')
        figure.height = 7
        print(f'После изменения высоты: {figure}\n')

"""
Теперь при изменении параметров при изменении атрибута height у объекта Square атрибут width меняется вместе с ним 
и наоборот. Расчеты периметра и площади подсчитаны верно. LSP не нарушается. 
"""

if __name__ == '__main__':
    main()
