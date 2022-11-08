class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps=0
        for i in word:
            if i.isupper():
                caps+=1
        if caps == len(word) or caps == 0 or (caps==1 and word[0].isupper()):
            return True
        return False
