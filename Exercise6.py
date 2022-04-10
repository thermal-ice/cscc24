"""
Exercise 6: Python operator overloading
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.numRows = len(matrix)
        self.numCols = len(matrix[0])

    def __str__(self):
        # what about
        # return  "shape:({0},{1})\n".format(self.numRows, self.numCols) + '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.matrix])
        return f"{self.numRows} x {self.numCols} Matrix:\n" \

    def __add__(self, other):
        
        if isinstance(other, self.__class__):
            if self.numCols != other.numCols or self.numRows != other.numRows:
                raise ValueError("Number of columns and rows in both matrices don't match")
            
            outerArr = []
            for i in range(self.numRows):
                tempRowArr = []
                for j in range(self.numCols):
                    tempRowArr.append(self.matrix[i][j] + other.matrix[i][j])

                outerArr.append(tempRowArr)

            return Matrix(outerArr)

        if isinstance(other, int):
            # should I expand this like urs?
            return Matrix([[self.matrix[i][j]+other for j in range(self.numCols)]
                            for i in range(self.numRows)])



# Running a script test
matrix1 = Matrix([[1, 2],
                  [3, 4]])

matrix2 = Matrix([[2, 2],
                  [2, 2]])

matrix3 = matrix1 + matrix2
matrix3 = matrix1 + 5
print(matrix3)
