"Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». "
"В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год"
"и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию "
"числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."


class Date:
    day: int
    month: int
    year: int

    # @classmethod
    # def convert_to_number(cls):

    def __init__(self, date_string: str):
        numbers = Date.convert_to_number(date_string)
        self.validate_numbers(numbers)

        self.day, self.month, self.year = numbers

    @classmethod
    def convert_to_number(cls, date_string: str):
        return [int(n) for n in date_string.split('.')]

    @staticmethod
    def validate_numbers(numbers: list):
        d, m, y = numbers

        assert 1 <= d <= 31, "Введено неверное число месяца!"
        assert 1 <= m <= 12, "Введен неверный месяц!"
        assert 1901 <= y <= 2100, "Введен неверный год!"
        if m in [4,6,9,11] and d > 30:
            assert False, "Введено неверное число месяца, в месяце 30 дней!"
        if y % 4 != 0 and m == 2 and d > 28:
            assert False, "Введено неверное число месяца, год не високосный!"
        if y % 4 == 0 and m == 2 and d > 29:
            assert False, "Введено неверное число месяца, в високосном году в феврале 29 дней!"

my_date1 = Date('19.12.2022')
# my_date2 = Date('32.12.2022')
# my_date3 = Date('01.13.2022')
# my_date4 = Date('01.01.2202')
# my_date5 = Date('30.02.2022')
# my_date6 = Date('29.02.2020')
# my_date7 = Date('30.02.2020')
# my_date8 = Date('29.02.2022')
#my_date9 = Date('31.06.2022')

