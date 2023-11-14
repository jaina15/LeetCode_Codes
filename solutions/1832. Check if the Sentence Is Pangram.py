import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = dict.fromkeys(string.ascii_lowercase, 0)
        for c in sentence:
            d[c]+=1
        for k,v in d.items():
            if v==0:
                return False
        return True
