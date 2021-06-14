class Solution:
    def mostCompetitive(self, a: List[int], k: int) -> List[int]:
        stack=[]
        c=0
        
        for i in range(len(a)):
            while stack and stack[-1] > a[i] and (len(a)-i-1)+len(stack)>=k:
                stack.pop()
            stack.append(a[i])
            #if len(stack)==k:
            #    break
        return stack[:k]
