class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        stack=[]
        for i in a:
            while stack and i < 0 < stack[-1]:
                if stack[-1] < -i:
                    stack.pop()
                    continue
                elif stack[-1] == -i:
                    stack.pop()
                break
            else:
                stack.append(i)
        return stack
