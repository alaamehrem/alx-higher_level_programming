#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for col in rows:
            if col ==rows[-1]:
                print("{:d}".format(col),end = "")
            else:
                print("{:d}".format(col),end = " ")
        print()
