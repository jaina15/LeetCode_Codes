from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        s=set()
        for k,v in cnt.items():
            s.add(v)
        return len(cnt)==len(s)
