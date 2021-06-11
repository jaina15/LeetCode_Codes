class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        #:(
        stack=[]
        d=0
        for i in range(1,target[-1]+1):
            stack.append('Push')
            if i != target[d]:
                stack.append('Pop')
            else:
                d+=1
        
        return stack
