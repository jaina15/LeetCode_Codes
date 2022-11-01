class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        #for i,v in enumerate(s):
        #    if v == ' ' and k>0:
        #        k-=1
        #    if k>=0 and i==len(s)-1:
        #        return s
        #    if k==0:
        #        return s[:i]
            
        return " ".join(s.split()[:k])
