class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt=0
        a = set(allowed)
        for w in words:
            wd = set(w)
            if wd.issubset(a):
                cnt+=1
        return cnt
