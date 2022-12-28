def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if abs(a // 100) < 1:
        if a % 2 == 0:
            mes = "two-digit even number"
        else:
            mes = "two-digit odd number"
    if abs(a // 100) >= 1:
        if a % 2 == 0:
            mes = "three-digit even number"
        else:
            mes = "three-digit odd number"
    return mes

print(main(10))