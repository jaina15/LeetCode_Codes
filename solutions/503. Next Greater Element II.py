class Solution:
    def nextGreaterElements(self, a: List[int]) -> List[int]:
        stack=[]
        left=[]
        right=[]
        
        for i in range(len(a)):
            if i==0:
                stack.append(i)
                left.append(-1)
            else:
                while stack and a[stack[-1]]<=a[i]:
                    stack.pop()
                if not stack:
                    left.append(-1)
                    stack.append(i)
                else:
                    left.append(stack[-1])
                    
                    #stack.append(i)
        stack.clear()
        for i in range(len(a)-1,-1,-1):
            if i==len(a)-1:
                stack.append(i)
                right.append(-1)
            else:
                while stack and a[stack[-1]]<=a[i]:
                    stack.pop()
                if not stack:
                    right.append(-1)
                    stack.append(i)
                else:
                    right.append(stack[-1])
                    stack.append(i)
        right=right[::-1]
        print(left)
        print(right)
        
        stack.clear()
        
        for i in range(len(a)):
            if right[i]==-1:
                stack.append(-1)
            else:
                stack.append(a[right[i]])
        print(stack)
        
        for i in range(len(a)):
            if left[i]==-1 or (left[i]!=-1 and right[i]!=-1):
                continue
            else:
                stack[i]=a[left[i]]
        print(stack)
        
        return stack
