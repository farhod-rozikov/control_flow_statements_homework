def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    pos_count = 0
    answer =  ''
    if a > 0:
        pos_count += 1
    if b > 0:
        pos_count += 1
    if c > 0:
        pos_count += 1    

    if pos_count > 1:
        answer = "there are a lot of positive numbers"
    else:
        answer = "there are a lot of negative numbers"
    return answer

print(main(1,-3,4))