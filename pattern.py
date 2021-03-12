"""
    This file is for pattern making
"""
def pattern(num):
    """
        This function takes a number as an argument print a pattern with n rows.
    """
    for i in range(1, num):
        if i in [1, num-1]:
            print('*' * (num - 1))
            continue
        for j in range(1, num):
            if (i == j) or (i + j == num):
                print('*', end= '')
            elif j in [1, num-1]:
                print('*', end='')
            else:
                print(' ', end= '')
        print()

pattern(10)
