def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Делитель не может быть нулем")
    return a / b

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    print(add(23, 67))
    print(subtract(55, 22))
    print(multiply(11, 11))
    n = divide(428, 4)
    if is_prime(n) == True:
        res = "prime"
    else:
        res = "not prime"
    print(f"The result of deviding 428 and 4 is {n}, \n {n} is {res}.")