def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    neg_count = 0
    if a < 0:
        neg_count += 1
    if b < 0:
        neg_count += 1
    if c < 0:
        neg_count += 1
    return neg_count

print(main(-1,2,-3))