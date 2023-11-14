class Solution:
    def checkString(self, s: str) -> bool:
        ass,bss=[],[]
        for i,c in enumerate(s):
            if c=='a':
                ass.append(i)
            elif c=='b':
                bss.append(i)
        
        if ass and bss and max(ass)>min(bss):
            return False
        return True
