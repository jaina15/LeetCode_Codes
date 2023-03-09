class Solution:
    def sortSentence(self, s: str) -> str:
        l=s.split(" ")
        lis=[]
        for w in l:
            lis.append((w[:-1],w[-1:]))
        lis=sorted(lis,key=lambda x:x[1])
        
        return ' '.join([w[0] for w in lis])
