class Solution:
    def sortSentence(self, s: str) -> str:
        word = s[::-1].split()
        return ' '.join([w[1:][::-1] for w in sorted(word)])
