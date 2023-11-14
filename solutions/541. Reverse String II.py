class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        words = [s[i:i + 2*k] for i in range(0, len(s), 2*k)]
        ans=''
        for word in words:
            if len(word)>=k:
                ans+=word[0:k][::-1]+word[k:]
            else:
                ans+=word[::-1]
        return ans
