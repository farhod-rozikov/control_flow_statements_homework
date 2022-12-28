def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    pos_count = 0
    if a > 0:
        pos_count += 1
    if b > 0:
        pos_count += 1
    if c > 0:
        pos_count += 1
    return pos_count

print(main(-1,2,-3))