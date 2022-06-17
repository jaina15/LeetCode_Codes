import string
class Solution:
    def checkIfPangram(self, s: str) -> bool:
        d = dict.fromkeys(string.ascii_lowercase, 0)
        for i in s:
            d[i]+=1
        for i in d:
            if d[i]==0:
                return False
        return True
