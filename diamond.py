#diamond pyramid
def diamond_pattern(row):

    # Upper pyramid
    for i in range(1 , row + 1, 2):
        print(' ' * ((row - i) // 2) + '*' * i )

    # Lower inverted pyramid
    for i in range(row - 2, 0, -2):
        print(' ' * ((row - i) // 2) + '*' * i )

#use an odd number for symmetry
diamond_pattern(9)