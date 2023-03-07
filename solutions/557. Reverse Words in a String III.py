class Solution:
    def reverseWords(self, s: str) -> str:
        res=''
        l=0
        for i in range(len(s)):
            if s[i]==' ' or i==len(s)-1:
                r=i
                if i==len(s)-1:
                    res+=" "
                for j in range(r,l-1,-1):
                    res+=s[j]
                #res+=" "
                l=i+1
        return res.strip()
