def printPascalTriangle(rows):
    triangle = []

    for row in range(1, rows + 1):
        c = 1

        numbers = []

        for i in range(1, row + 1):
            numbers.append(c)
            c = c * (row - i) // i

        triangle.append(numbers)

        last_row = triangle[-1]
        number_width = len(str(max(last_row))) + 1
        triangle_width = number_width * len(last_row)

        for row in triangle:
            string = ""

            for number in row:
                number_string = str(number)
                string += number_string + " " * (number_width - len(number_string))

        print(string.center(triangle_width))


printPascalTriangle(8)
