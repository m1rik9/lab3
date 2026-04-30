def sequence_iterative(n):
    """Итеративное вычисление n-го члена."""
    if n <= 0:
        return None
    if n <= 3:
        return 1
    
    x1, x2, x3 = 1, 1, 1
    for i in range(4, n + 1):
        x_next = x3 + x1
        x1, x2, x3 = x2, x3, x_next
    return x3


def sequence_recursive(n):
    """Рекурсивное вычисление n-го члена."""
    if n <= 0:
        return None
    if n <= 3:
        return 1
    return sequence_recursive(n - 1) + sequence_recursive(n - 3)


# Проверка работы функций
print("n = 1:", sequence_iterative(1), sequence_recursive(1))
print("n = 2:", sequence_iterative(2), sequence_recursive(2))
print("n = 3:", sequence_iterative(3), sequence_recursive(3))
print("n = 4:", sequence_iterative(4), sequence_recursive(4))