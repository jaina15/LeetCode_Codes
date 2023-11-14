class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        words = [[word[:-1],word[-1]] for word in words]
        lis=sorted(words,key=lambda x:x[1])
        return ' '.join([word[0] for word in lis])
