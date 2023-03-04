class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c=0
        for word in words:
            if word[:len(pref)]==pref:
                c+=1
        return c
