import sympy as sp


class NewtonMethod:
    def __init__(self, f, x0, tol=1e-6, max_iter=1000):
        self.f = f
        self.x0 = x0
        self.tol = tol
        self.max_iter = max_iter

    def solve(self):
        x = self.x0
        iter_count = 0
        f = sp.lambdify('x', self.f)
        f_prime = sp.lambdify('x', sp.diff(self.f, 'x'))

        while iter_count < self.max_iter:
            fx = f(x)
            if abs(fx) < self.tol:
                return x
            dfx = f_prime(x)
            if dfx == 0:
                raise ValueError("Производная равна нулю. Метод Ньютона не может быть применен.")
            x = x - fx / dfx
            iter_count += 1
        raise ValueError("Метод Ньютона не сошелся за максимальное количество итераций.")


def get_function_from_input():
    func_str = input("Введите функцию (например, 'x**3 - 2*x - 5'): ")
    f = sp.sympify(func_str)
    return f


if __name__ == "__main__":
    f = get_function_from_input()
    x0 = float(input("Введите начальное приближение: "))

    newton = NewtonMethod(f, x0)
    root = newton.solve()
    print("Приближенный корень:", root)
