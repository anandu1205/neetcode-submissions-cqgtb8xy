class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows=rowIndex+1
        triangle=[[1]*(i+1) for i in range(0,numRows+1)]
        for i in range(2,numRows+1):
            for j in range(1,i):
                triangle[i][j]=triangle[i-1][j]+triangle[i-1][j-1]
        return triangle[numRows-1]
        
        