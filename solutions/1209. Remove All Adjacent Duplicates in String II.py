class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #hmmmmmmmmmmmmmmmmmmmm mene dictiondary s try kia tha, but usme pips wale TC me fail horha tha bar bar
        #kyunki me char ka count toh nikal rha tha but agar ek character k bad dusr character stack me store hogya
        #jiska count k ke equal nhi hua or uske baad pehle wale character k k times entry aati h to dictionary me 
        #vo pehle wale character ka bhi count rakh rha tha, jiski wajah s galat output aarha tha.
        stack=[['#',0]]
        for i in s:
            if stack[-1][0]==i:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([i,1])
        
        #print(stack)
        return ''.join(k*v for k,v in stack)
