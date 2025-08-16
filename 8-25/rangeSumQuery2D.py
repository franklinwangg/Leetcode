class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dynamic = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            soFar = 0
            for j in range(len(matrix[0])):
                soFar += matrix[i][j]
                self.dynamic[i][j] = soFar

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        # for i in range(col1, col2):
            # row1Sum = 0
            # if(row1 != 0):
            #     row1Sum = self.dynamic[i][row1 - 1]
            # rowSum = self.dynamic[i][row2] - row1Sum
        #     total += rowSum
        for i in range(row1, row2 + 1):
            row1Sum = 0
            if(col1 != 0):
                row1Sum = self.dynamic[i][col1 - 1]
            rowSum = self.dynamic[i][col2] - row1Sum
            total += rowSum
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)