class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # corner case
        if len(matrix) == 0 or len(matrix[0]) == 0: return
        r,c = len(matrix), len(matrix[0])
        # pre-computation TC: o(nm) ; sc: o(nm)
        self.dp = [[0 for _ in range(c+1)] for _ in range(r+1)]
        for _r in range(1,r+1):
            for _c in range(1,c+1):
                self.dp[_r][_c] = self.dp[_r-1][_c] + self.dp[_r][_c-1] - self.dp[_r-1][_c-1] + matrix[_r-1][_c-1] 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # o(1) per query
        return self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - self.dp[row1][col2+1] + self.dp[row1][col1] 
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)