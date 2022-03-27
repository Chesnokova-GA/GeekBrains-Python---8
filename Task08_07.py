"7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», "
"реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, "
"создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. "
"Проверьте корректность полученного результата."

class ComplexNumber:
    real: float
    indeterminate: float

    def __init__(self, real: float, indeterminate: float):
        self.real = real
        self.indeterminate = indeterminate

    def __add__(self, other: 'ComplexNumber'):
        return ComplexNumber(
            self.real + other.real,
            self.indeterminate + other.indeterminate
        )

    def __mul__(self, other: 'ComplexNumber'):
        r1 = self.real * other.real
        r2 = self.indeterminate * other.indeterminate * -1

        i1 = self.real * other.indeterminate
        i2 = self.indeterminate * other.real

        real = r1 + r2
        indeterminate = i1 + i2

        return ComplexNumber(real, indeterminate)

    def __str__(self):
        return f"({self.real}{'+' if self.indeterminate > 0 else ''}{self.indeterminate}i)"


x = ComplexNumber(3, 27)
y = ComplexNumber(17, 42)

# (3+27i) + (17+42i) = (3 + 17) + (27 + 42)i = (20+69i)
print(x + y)

# (3+27i) * (17+42i) = (3 * 17) + (3 * 42i) + (17 * 27i) + (27 * 42* i^2) = 51 + 126i + 459i - 1134 = (-1083+585i)
print(x * y)