class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for i in operations:
            if i in ('X++','++X'):
                x+=1
            elif i in ('X--','--X'):
                x-=1
        return x
