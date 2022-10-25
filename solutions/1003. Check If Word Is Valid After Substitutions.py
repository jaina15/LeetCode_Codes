class Solution:
    def isValid(self, s: str) -> bool:
        while len(s)>0:
            if 'abc' in s:
                s=s.replace('abc','')
            else:
                return False
        return True if len(s)==0 else False
