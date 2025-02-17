class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return[[1]]
        l=[[1]]
        for i in range(1,numRows):
            x=[1]
            for j in range(1,i):
                x.append(l[i-1][j-1]+l[i-1][j])
            x.append(1)
            l.append(x)
        return l

