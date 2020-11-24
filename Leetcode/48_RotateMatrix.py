class Solution:
    def rotate(self, matrix):
        matrix=self.transpose(matrix)

    def verticalReflection(self,t_matrix):
        m = len(t_matrix)
        n = len(t_matrix[0])
        for i in range(n // 2):
            for j in range(m):
                t_matrix[j][i], t_matrix[j][m - (i + 1)] = t_matrix[j][m - (i + 1)], t_matrix[j][i]
        return t_matrix

    def transpose(self,inpMatrix):
        m = len(inpMatrix)
        n = len(inpMatrix[0])
        for i in range(m):
            for j in range(i, n):
                inpMatrix[i][j], inpMatrix[j][i] = inpMatrix[j][i], inpMatrix[i][j]

        return self.verticalReflection(inpMatrix)