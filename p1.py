def is_palindrome_iterative(seq):
    """Итеративная проверка палиндрома."""
    left, right = 0, len(seq) - 1
    while left < right:
        if seq[left] != seq[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome_recursive(seq):
    """Рекурсивная проверка палиндрома."""
    if len(seq) <= 1:
        return True
    if seq[0] != seq[-1]:
        return False
    return is_palindrome_recursive(seq[1:-1])


# Проверка работы функций
print(is_palindrome_iterative([1, 2, 3, 2, 1]))
print(is_palindrome_iterative('spam'))
print(is_palindrome_recursive([1, 2, 3, 2, 1]))
print(is_palindrome_recursive('spam'))