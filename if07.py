def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a > 0:
        if a % 2 == 0:
            mes = "positive even number"
        else:
            mes = "positive odd number"
    if a < 0:
        if a % 2 == 0:
            mes = "negative even number"
        else:
            mes = "negative odd number"
    if a == 0:
        mes = "the number is zero"

    return mes

print(main(-1))