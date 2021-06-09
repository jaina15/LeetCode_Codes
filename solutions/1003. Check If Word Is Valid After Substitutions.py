class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            p=s.find('abc')
            if p>=0:
                s=s.replace('abc','')
                #print(s)
                if s=='':
                    return True
            else:
                return False
