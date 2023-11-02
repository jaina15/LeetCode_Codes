from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt1,cnt2= Counter(words1),Counter(words2)
        ans = 0
        if len(cnt1)<len(cnt2):
            for k,v in cnt1.items():
                if k in cnt2 and v == 1 and cnt2[k] == 1:
                    ans+=1
                    
        else:
            for k,v in cnt2.items():
                if k in cnt1 and v == 1 and cnt1[k] == 1:
                    ans+=1
        return ans
