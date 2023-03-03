class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacks,stackt=[],[]
        for i in s:
            if stacks and i=='#':
                stacks.pop()
            elif i!='#':
                stacks.append(i)
        
        for i in t:
            if stackt and i=='#':
                stackt.pop()
            elif i!='#':
                stackt.append(i)
        return ''.join(stacks)==''.join(stackt)
