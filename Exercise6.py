"""
Exercise 6: Python operator overloading
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.numRows = len(matrix)
        self.numCols = len(matrix[0])

    def dotProduct(self,vec1: list, vec2: list):
        if len(vec1) != len(vec2):
            return "Invalid operation: different vector lengths"

        dotProdSum = 0
        for i in range(len(vec1)):
            dotProdSum += vec1[i] * vec2[i]

        return dotProdSum

    def getRow(self, rowNum: int):
        if rowNum < 0 or rowNum > self.numRows:
            return "invalid index for rows"
        return self.matrix[rowNum]

    def getCol(self, colNum: int):
        if colNum < 0 or colNum > self.numCols:
            return "invalid index for columns"

        retCol = []
        for i in range(self.numRows):
            retCol.append(self.matrix[i][colNum])

        return retCol

    def __invert__(self):
        transposeMatrix = []
        for i in range(self.numCols):
            transposeMatrix.append(self.getCol(i))

        return Matrix(transposeMatrix)

    def __scalarMult(self, scalarVal):
        multArr = []
        for row in self.matrix:
            tempRowArr = []
            for cellVal in row:
                tempRowArr.append(cellVal * scalarVal)
            multArr.append(tempRowArr)
        return Matrix(multArr)

    def __neg__(self):
        return self.__scalarMult(-1)

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self.__scalarMult(other)

        return "Invalid multiplication operation"

    def __mul__(self, other):
        if isinstance(other, self.__class__):

            if self.numCols != other.numRows:
                return "Invalid dimensions for matrix multiplication"

            multiplicationArr = []
            for i in range(self.numRows):
                tempRowArr = []
                for j in range(other.numCols):
                    dotProdRes = self.dotProduct(self.getRow(i),other.getCol(j))
                    tempRowArr.append(dotProdRes)

                multiplicationArr.append(tempRowArr)

            return Matrix(multiplicationArr)

        if isinstance(other, (int, float)):
            return self.__scalarMult(other)

        return "Invalid operation type"


    def __str__(self):
        # what about
        return  "shape:({0},{1})\n".format(self.numRows, self.numCols) + '\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in self.matrix])
        # return f"{self.numRows} x {self.numCols} Matrix:\n" \
        #        f"{self.matrix}"

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[self.matrix[i][j] + other for j in range(self.numCols)]
                           for i in range(self.numRows)])
        return "Invalid addition operation. Type isn't plus"

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
            return Matrix([[self.matrix[i][j]+other for j in range(self.numCols)]
                            for i in range(self.numRows)])



# Running a script test
matrix1 = Matrix([[1, 2],
                  [3, 4]])

matrix2 = Matrix([[2, 2],
                  [2, 2]])

matrix3 = matrix1 + matrix2
matrix4 = 5+ matrix1
print(matrix3)
print(matrix4)
matrix5 = Matrix([[5,6],
                 [7,8]])



# print(matrix1.getCol(1))
print(-2 *(matrix1 * matrix5))