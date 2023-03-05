class Solution:
    def reverseVowels(self, s: str) -> str:
        l,r=0,len(s)-1
        v=['a','e','i','o','u']
        s=list(s)
        lv,rv=0,0
        while l<r:
            if s[l].lower() in v:
                lv=1
            else:
                l+=1
            if s[r].lower() in v:
                rv=1
            else:
                r-=1
            if lv and rv:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
                lv,rv=0,0
        return ''.join(s)
