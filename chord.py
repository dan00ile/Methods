class ChordMethod:
    def __init__(self, f, a, b, tol=1e-6, max_iter=1000):
        self.f = f
        self.a = a
        self.b = b
        self.tol = tol
        self.max_iter = max_iter

    def solve(self):
        if self.f(self.a) * self.f(self.b) > 0:
            raise ValueError("Функция имеет одинаковые знаки на концах интервала. Метод хорд не может быть применен.")

        iter_count = 0
        while iter_count < self.max_iter:
            c = self.a - self.f(self.a) * (self.b - self.a) / (self.f(self.b) - self.f(self.a))
            if abs(self.f(c)) < self.tol:
                return c
            if self.f(c) * self.f(self.a) < 0:
                self.b = c
            else:
                self.a = c
            iter_count += 1
        raise ValueError("Метод хорд не сошелся за максимальное количество итераций.")


def get_function_from_input():
    func_str = input("Введите функцию (например, 'x**3 - 2*x - 5'): ")
    return lambda x: eval(func_str)


if __name__ == "__main__":
    func = get_function_from_input()
    a = float(input("Введите нижний интервал: "))
    b = float(input("Введите верхний интервал: "))

    chord = ChordMethod(func, a, b)
    root = chord.solve()
    print("Приближенный корень:", root)
