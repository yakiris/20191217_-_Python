# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте
# относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Dress(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

class Coat(Dress):
    def __init__(self, size):
        super().__init__(self)
        self.size = size
    def calculation(self):
        return round(self.size / 6.5 + 0.5, 2)

class Suit(Dress):
    def __init__(self, height):
        super().__init__(self)
        self.height = height
    def calculation(self):
        return round(2*self.height + 0.3, 2)

size = 48
height = 1.75
c = Coat(size)
print(f'Расход ткани на пальто {size} размера = {c.calculation()} метра(ов)')
s = Suit(height)
print (f'Расход ткани на костюм на рост {height} = {s.calculation()} метра(ов)')
print(f'Общий расход ткани = {c.calculation() + s.calculation()} метра(ов)')
