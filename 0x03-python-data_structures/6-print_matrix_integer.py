#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
<<<<<<< HEAD
    """Print a matrix of integers."""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                print("{:d}".format(matrix[i][j]), end="")
                if j != (len(matrix[i]) - 1):
                    print(" ", end="")

        print("")
=======
    if matrix != [[]]:
        for row in matrix:
            for elem in row:
                print("{:d}".format(elem), end=" "
                      if elem != row[-1] else '\n')
    else:
        print()
>>>>>>> 5655493bd104b56a9d555e1639a5eb2c50487745
