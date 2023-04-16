import trapezoid_method


def main():
    print("Выберите уравнение:\n"
          "1. 1/x\n"
          "2. sin(0.001)/0.001 + sin(-0.001)/-0.001/2\n"
          "3. x^2 + 2\n"
          "4. 2x+2")
    variant = int(input())
    print("Введите левую границу интервала")
    a = int(input())
    print("Введите правую границу интервала")
    b = int(input())
    print("Введите точность")
    epsilon = float(input())
    result = trapezoid_method.calculate_integral(a=a, b=b, f=variant, epsilon=epsilon)
    print(f'Результат: {result}')


if __name__ == '__main__':
    main()
