# Задачи пары: раунд 2 — fizzbuzz, раунд 3 — is_prime.

# Вместо ... впишите своё имя, вместо raise NotImplementedError — решение.
# Проверить, что файл запускается без ошибок: python3 tasks.py


def fizzbuzz(n):
    if (n % 3 == 0 and n % 5 == 0):
        return "Fizzbuzz"
    if (n % 3 == 0):
        return "Fizz"
    if (n % 5 == 0):
        return "Buzz"
    else:
        return n

        
    """Вернуть "FizzBuzz", если n делится на 3 и на 5, "Fizz" — только на 3,
    "Buzz" — только на 5, иначе само число строкой.

    Примеры:
        fizzbuzz(9) -> "Fizz"
        fizzbuzz(10) -> "Buzz"
        fizzbuzz(15) -> "FizzBuzz"
        fizzbuzz(7) -> "7"
    """
    # Реализовал(а): Daria
    # Реализовал(а): ...
    raise NotImplementedError


def is_prime(n):
    for i in range(2, sqrt(n)+1):
        if n%i==0:
            return False
    return True
    # Реализовал(а): Daria
    raise NotImplementedError
