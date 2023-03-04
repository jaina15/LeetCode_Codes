class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans=0
        for i in range(len(mat)):
            #print(mat[i][i],mat[i][len(mat)-i-1])
            ans+=mat[i][i]+mat[i][len(mat)-i-1]
        return ans-mat[len(mat)//2][len(mat)//2] if len(mat)%2==1 else ans
