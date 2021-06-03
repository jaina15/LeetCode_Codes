class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        
        for i in asteroids:
            if not stack:
                stack.append(i)
            else:
                if stack[-1]<i:
                    stack.append(i)
                elif stack[-1]+i>0 and i<0 and stack[-1]>0:
                    pass
                elif stack[-1]+i<0 and i<0 and stack[-1]>0:
                    
                    while stack[-1]+i<0 and i<0 and stack[-1]>0:
                        stack.pop()
                        if not stack:
                            break
                        #print(stack)
                    
                    stack.append(i)
                    #print(stack)
                    if len(stack)>1:
                        while stack[-2]+stack[-1]>0 and stack[-1]<0 and stack[-2]:
                            stack.pop()
                            if len(stack)==1:
                                break
                            
                        while stack[-1]<0 and stack[-2]==-stack[-1] and stack[-2]>0:
                            #print(stack)
                            stack.pop()
                            stack.pop()
                            #print(stack)
                            if len(stack)<=1:
                                break
                        
                elif stack[-1]+i==0 and i<0:
                    stack.pop()
                else:
                    stack.append(i)
                    #print(stack)
                    
        return stack
