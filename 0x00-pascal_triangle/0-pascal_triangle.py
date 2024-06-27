#!/usr/bin/python3
""" Returns a list of lists of integers. """


def factorial(n):
    """ Factorial function. """
    # Base condition to end recursion
    if n == 0:
        return 1
    else:  # n is greater than 0
        return (n * factorial(n-1))


def comb(a, b):
    """ Calculate combination of 2 numbers. """
    # Floor division to get integer as classic division returns float value
    return factorial(a) // (factorial(b) * (factorial(a - b)))


def pascal_triangle(n):
    """ Representing the Pascals triangle of n. """
    # Define matrix
    matrix = []

    # Empty list if n is less than or equal to 0
    if n <= 0:
        return matrix

    # n stands for number of rows so we loop through n
    for x in range(n):
        # Define inner list
        new = []
        for y in range(x + 1):
            # Find the combination of x and y
            result = comb(x, y)
            # Append result to inner list
            new.append(result)
        # Append inner list to matrix
        matrix.append(new)
    # Return list of list
    return matrix

#!/usr/bin/python3
#def pascal_triangle(n):
#    if n <= 0:
#        return []

#    triangle = [[1]]
#    for i in range(1, n):
#        row = [1]
#        for j in range(1, i):
#            row.append(triangle[i-1][j-1] + triangle[i-1][j])
#        row.append(1)
#        triangle.append(row)
#
#    return triangle
