# Объявляем класс stationery
class Stationery:
    title = 'Канцелярские принадлежности'

    def draw(self):
        print(f'Запуск отрисовки')

    def __init__(self):
        pass

# Объявляем дочерние классы и переопределяем метод draw
class Pen(Stationery):
    def draw(self):
        print(f'Рисуем ручкой {self.manufacturer}')
    
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем карандашом {self.manufacturer}')
    
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

class MarkerPen(Stationery):
    def draw(self):
        print(f'Рисуем маркером {self.manufacturer}')

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer


# Создаём объекты каждого класса и вызвываем соответствующий метод
any_stationery = Stationery()
any_stationery.draw()

a_pen = Pen('Parker')
a_pen.draw()

pen_2 = Pen('Erich Krause')
pen_2.draw()

a_pencil = Pencil('Kohinoor')
a_pencil.draw()

a_marker_pen = MarkerPen('Erich Krause')
a_marker_pen.draw()