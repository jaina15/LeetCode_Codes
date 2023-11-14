class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(s)!=len(words):
            return False
        for i,word in enumerate(words):
            if word[0]!=s[i]:
                return False
        return True
