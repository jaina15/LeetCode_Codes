from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        d=defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)
        for k,v in d.items():
            ans.append(v)
        return ans
