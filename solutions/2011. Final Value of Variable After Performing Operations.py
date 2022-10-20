class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        v=0
        for i in operations:
            if i in ('++X','X++'):
                v+=1
            elif i in ('--X','X--'):
                v-=1
        return v
