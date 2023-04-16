import math


class Result:
    error_message = ""
    has_discontinuity = False
    eps = 0.001

    def first_function(x: float):
        return 1 / x

    def second_function(x: float):
        if x == 0:
            return (math.sin(Result.eps) / Result.eps + math.sin(-Result.eps) / -Result.eps) / 2
        return math.sin(x) / x

    def third_function(x: float):
        return x * x + 2

    def fourth_function(x: float):
        return 2 * x + 2

    def five_function(x: float):
        return math.log(x)

    # How to use this function:
    # func = Result.get_function(4)
    # func(0.01)
    def get_function(n: int):
        if n == 1:
            return Result.first_function
        elif n == 2:
            return Result.second_function
        elif n == 3:
            return Result.third_function
        elif n == 4:
            return Result.fourth_function
        elif n == 5:
            return Result.five_function
        else:
            raise NotImplementedError(f"Function {n} not defined.")


def calculate_integral(a, b, f, epsilon):
    """
    Вычисляет приближенное значение интеграла от функции f на интервале [a, b]
    методом трапеций с заданной точностью epsilon.
    """
    f = Result.get_function(f)
    # Проверяем, что a < b
    if a >= b:
        return -(calculate_integral(b, a, f, epsilon))

    # Вычисляем количество трапеций, необходимых для достижения заданной точности
    n = 1
    integral_old = 0
    integral_new = (f(a) + f(b)) * (b - a) / 2
    while abs(integral_new - integral_old) > epsilon and n < 1e6:
        n *= 2
        h = (b - a) / n
        x = a + h
        s = 0
        for i in range(n - 1):
            s += f(x)
            x += h
        integral_old = integral_new
        integral_new = (integral_old + h * s) / 2

    # Проверяем, что функция не имеет устранимых разрывов первого рода
    try:
        f((a + b) / 2)
    except ValueError:
        Result.error_message = "Integrated function has discontinuity or does not defined in current interval"
        Result.has_discontinuity = True
        return None

    # Возвращаем приближенное значение интеграла и отметку о том, что разрывов нет
    Result.has_discontinuity = False
    return integral_new
