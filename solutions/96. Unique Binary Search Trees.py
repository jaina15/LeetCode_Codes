class Solution:
    def numTrees(self, n: int) -> int:
        #catalan number ( 2n!/(n+1)!*n! )
        return factorial(2*n)//factorial(n+1)//factorial(n)
