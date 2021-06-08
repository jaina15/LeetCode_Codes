class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        l=len(popped)
        c=0
        i=0
        pos=0
        while i<len(pushed):
            if popped and pushed and pushed[i]==popped[0]:
               # pos=i
                while popped and pushed and pushed[i]==popped[0]:
                    popped.pop(0)
                    c+=1
                    pushed.pop(i)
                    i-=1
                #i=pos
                   # print(popped)
                   # print(pushed)
                    if not popped or i<0:
                        break
            i+=1
            #print(popped)
        if c==l:
            return True
        return False
