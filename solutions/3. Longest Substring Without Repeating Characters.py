class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,res=0,0
        charset = set()
        
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            res = max(res,r-l+1)
        return res
