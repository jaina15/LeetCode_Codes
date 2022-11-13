import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letter_count = dict( (key, 0) for key in string.ascii_lowercase )
        for char in sentence:
            if char in letter_count:
                letter_count[char]+=1
            else:
                letter_count[char]=1
        for k,v in letter_count.items():
            if v==0:
                return False
        return True
