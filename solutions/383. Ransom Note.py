from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt_a = Counter(ransomNote)
        cnt_b = Counter(magazine)
        
        for k,v in cnt_a.items():
            if v>cnt_b[k] or k not in cnt_b:
                return False
        return True
