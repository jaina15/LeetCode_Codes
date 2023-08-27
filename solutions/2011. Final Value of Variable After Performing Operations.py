class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for o in operations:
            if o in ['--X','X--']:
                x-=1
            elif o in ['X++','++X']:
                x+=1
        return x
