"4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. "
"А также класс «Оргтехника», который будет базовым для классов-наследников. "
"Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). "
"В базовом классе определить параметры, общие для приведенных типов. " 
"В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники."

class Sklad:
    __storage = []

    def add_to(self, equipment):
       self.__storage.append(equipment)

class OfficeEquipment:
    def __init__(self, type: str, model: str, cost: float, sn: str):
        self.type = str(type)
        self.model = str(model)
        self.cost = float(cost)
        self.sn = str(sn)

    def __str__(self):
        return f"{self.type} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, model: str, cost: float, is_colorful: bool, sn: str):
        self.is_colorful = is_colorful
        super().__init__('Принтер', model, cost, sn)


class Scanner(OfficeEquipment):
    def __init__(self, model: str, cost: float, dpi: str, sn: str):
        self.dpi = dpi
        super().__init__('Сканер', model, cost, sn)


class Xerox(OfficeEquipment):
    def __init__(self, model: str, cost: float, is_colorful: bool, dpi: str, velocity: int, sn: str):
        self.is_colorful = is_colorful
        self.dpi = dpi
        self.velocity = velocity
        super().__init__('МФУ', model, cost, sn)


if __name__ == '__main__':
    printer01 = Printer('Epson L120', 1000.99, True, 'N8PS568493706')
    printer02 = Printer('HP Laser 107', 8999.90, False, 'H85U277R567')
    scanner01 = Scanner('Canon LiDE 1200', 2100.45, True, '2400x2400')
    xerox01 = Xerox('Canon PIXMA MG2540S', 4499.90, True, '4800x600', 8, 'RW85456AS4155')
    xerox02 = Xerox('Canon i-sensys LBP6020B', 19100, False, '2400x600', 30, '78VCX45451ZQ245')
    xerox03 = Xerox('HP LaserJet M132nw', 14500, False, '1200x1200', 22, 'AS85545POI5512')

sklad = Sklad()
sklad.add_to(printer01)
sklad.add_to(printer02)
sklad.add_to(scanner01)
sklad.add_to(xerox01)
sklad.add_to(xerox02)
sklad.add_to(xerox03)