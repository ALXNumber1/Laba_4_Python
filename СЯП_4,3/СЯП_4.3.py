class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"{self.title}: Начинаем писать ручкой")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title}: Рисуем карандашом")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title}: Работаем маркером")


pen_instance = Pen("Ручка")
pencil_instance = Pencil("Карандаш")
handle_instance = Handle("Маркер")

pen_instance.draw()
pencil_instance.draw()
handle_instance.draw()
