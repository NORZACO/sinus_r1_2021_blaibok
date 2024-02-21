# pylint: disable=missing-module-docstring
def grenseverdier_test1():
    def f(x):
        return 3 * x - 3

    svar = input("Velg verdi for a: ")
    # change input to float type
    a = float(svar)
    print(f"Your answer change to float: {a}")

    t = 0.1
    while t > 0.0000001:
        print(f"f({str(round(a - t, 7))}) = {round(f(a - t), 7)}")
        t = t / 10

    t = 0.1
    while t > 0.0000001:
        print(f"f({str(round(a + t, 7))}) = {round(f(a + t), 7)}")
        t = t / 10

# grenseverdier_test1()



def grenseverdier_test2():
    """
    docstring
    """

    def f(x):
        print(pow(x, 3) + 2 * pow(x, 2))
        return pow(x, 3) + 2 * pow(x, 2)

    svar = input("Velg verdi for a : ")
    a = float(svar)

    t = 0.1
    while t > 0.0000001:
        print(f"f({str(round(a - t, 7))}) = {round(f(a - t), 7)}")
        t = t / 10
        # print(f"-->T/10 = {t/10}")

    t = 0.1
    while t > 0.0000001:
        print(f"f({str(round(a + t, 7))}) = {round(f(a + t), 7)}")
        t = t / 10
        # print(f"-->T/10 = {t/10}")


# grenseverdier_test2()


def grenseverdier_test3():
    # tilpass programmet, og finn tilnærmingverdier for lim x--->a (x^3 + 2x^2 + 3x - 6)
    def f(x):
        f_value = pow(x, 3) + pow(2 * x, 2) - 6
        print(f_value)
        return f_value

    svar = input("Enter the value of a : ")
    # change to float
    a = float(svar)

    t = 0.1
    while t > 0.0000001:
        tilnærmingsverdier = f"f({str(round(a - t, 7))}) = {round(f(a - t), 7)}"
        print(tilnærmingsverdier)
        t / 10

    while t > 0.0000001:
        tilnærmingsverdier = f"f({str(round(a + t, 7))}) = {round(f(a + t), 7)}"
        print(tilnærmingsverdier)
        t / 10


def grenseverdier_test4():
    # tilpass programmet, og finn tilnærmingverdier for lim x--->a (x^3 + 2x^2 + 3x - 6)
    def funksjon(x):
        f_value = pow(x, 3) + 2 * pow(x, 2) + 3 * x - 6
        # print(f_value)
        return f_value

    svar = input("Enter the value of a : ")
    # change to float
    a = float(svar)

    t = 0.1
    while t > 0.0000001:
        tilnærmingsverdier = (f"funksjon({str(round(a - t, 7))}) = { round(funksjon(a - t), 7) }")
        print(tilnærmingsverdier)
        t / 10

    t = 0.1
    while t > 0.0000001:
        tilnærmingsverdier = (
            f"funksjon({str(round(a + t, 7))}) = { round(funksjon(a + t), 7) }"
        )
        print(tilnærmingsverdier)
        t / 10


def grenseverdier_test5():
    def f(x):
        f_value = 3 * pow(x, 3) + 2 * (x, 2)
        return f_value

    a = float(input("Enter the verdi a: "))

    t = 0.1
    while t > 0.0000001:
        print(f"f({str(round(a - t, 7))}) = { round(f(a - t), 7 )}")
        t/10

    t = 0.1
    while t > 0.0000001:
        print(f"f{str(round(a + t, 7))} = { round(f(a + t), 7) }")
        t/10

grenseverdier_test5()


