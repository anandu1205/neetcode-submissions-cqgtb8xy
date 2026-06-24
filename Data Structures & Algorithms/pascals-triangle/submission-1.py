class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[[1]*(i+1) for i in range(0,numRows)]
        for i in range(2,numRows):
            for j in range(1,i):
                triangle[i][j]=triangle[i-1][j]+triangle[i-1][j-1]
        return triangle
        