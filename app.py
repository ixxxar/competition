def factorial(n):
    if n < 0:
        return "Факториал отрицательного числа не определен"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

def factoria2l(n):
    if n < 0:
        return "Факториал отрицательного числа не определен"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

def factori3al(n):
    if n < 0:
        return "Факториал отрицательного числа не определен"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

def factori3al(n):
    if n < 0:
        return "Факториал отрицательного числа не определен"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

number = int(input("Введите число: "))
print(f"Факториал числа {number} равен {factorial(number)}")


def factorial2(n):
    if n < 0:
        return "Факториал отрицательного числа не определен"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

number = int(input("Введите число: "))

numb2er = int(input("Введите число: "))

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


number = int(input("Введите число: "))
if is_prime(number):
   print(f"{number} - простое число")
else:
   print(f"{number} - не является простым числом")

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


number = int(input("Введите число: "))
if is_prime(number):
   print(f"{number} - простое число")
else:
   print(f"{number} - не является простым числом")


def is_p2rime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


number = int(input("Введите число: "))
if is_prime(number):
   print(f"{number} - простое число")
else:
   print(f"{number} - не является простым числом")

def is_p2rime4(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


number = int(input("Введите число: "))
if is_prime(number):
   print(f"{number} - простое число")
else:
   print(f"{number} - не является простым числом")
def is_prim2e4(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


number = int(input("Введите число: "))
if is_prime(number):
   print(f"{number} - простое число")
else:
   print(f"{number} - не является простым числом")

