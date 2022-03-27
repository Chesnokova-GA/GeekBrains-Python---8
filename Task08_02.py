"2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, "
"вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту"
"ситуацию и не завершиться с ошибкой."


class DivisionByZero(Exception):
    pass

def get_numerator():
     value_numerator = int(input("Введите числитель >>> "))
     return value_numerator

def get_denominator():
    value_denominator = int(input("Введите знаменатель >>> "))
    if value_denominator == 0:
        raise DivisionByZero
    return value_denominator

while True:
    try:
        numerator = get_numerator()
        denominator = get_denominator()

        print(f"Результат от деления = {numerator / denominator}")
    except DivisionByZero:
        print("Деление на 0!")
    except KeyboardInterrupt:
        break