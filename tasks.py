# Задачи пары: раунд 2 — fizzbuzz, раунд 3 — is_prime.

# Вместо ... впишите своё имя, вместо raise NotImplementedError — решение.
# Проверить, что файл запускается без ошибок: python3 tasks.py



def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    
    """Вернуть "FizzBuzz", если n делится на 3 и на 5, "Fizz" — только на 3,
    "Buzz" — только на 5, иначе само число строкой.

    Примеры:
        fizzbuzz(9) -> "Fizz"
        fizzbuzz(10) -> "Buzz"
        fizzbuzz(15) -> "FizzBuzz"
        fizzbuzz(7) -> "7"
    """
    # Реализовал(а): Arina
    raise NotImplementedError


def is_prime(n):
    """Вернуть True, если n — простое число (больше 1 и делится только на 1 и на себя).

    Примеры:
        is_prime(13) -> True
        is_prime(9) -> False
        is_prime(1) -> False
    """
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

    # Реализовал(а): Arina
    raise NotImplementedError
