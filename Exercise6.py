"""
Exercise 6: Python operator overloading
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.numRows = len(matrix)
        self.numCols = len(matrix[0])

    def __str__(self):
        return f"{self.numRows} x {self.numCols} Matrix:\n" \
               f"{self.matrix}"

    def __add__(self, other):
        if self.numCols != other.numCols or self.numRows != other.numRows:
            raise ValueError("Number of columns and rows in both matrices don't match")

        if isinstance(other, self.__class__):
            outerArr = []
            for i in range(self.numRows):
                tempRowArr = []
                for j in range(self.numCols):
                    tempRowArr.append(self.matrix[i][j] + other.matrix[i][j])

                outerArr.append(tempRowArr)

            return Matrix(outerArr)

        if isinstance(other, int):
            return "will implement later"


# Running a script test
matrix1 = Matrix([[1, 2],
                  [3, 4]])

matrix2 = Matrix([[2, 2],
                  [2, 2]])

matrix3 = matrix1 + matrix2

print(matrix3)
