class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d=dict()
        for v,k in enumerate(groupSizes):
            if k not in d:
                d[k] = [v]
            else:
                d[k].append(v)
        ans=[]
        for k,v in d.items():
            if len(v)>=k:
                ans.extend([v[i:i + k] for i in range(0, len(v), k)] )
            else:
                ans.extend(v)
        print(ans)
        return ans
