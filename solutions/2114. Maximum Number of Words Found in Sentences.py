class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi=0
        for s in sentences:
            maxi = max(maxi,len(s.split()))
        return maxi
