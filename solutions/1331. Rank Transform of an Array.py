class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        h={}
        for v in sorted(arr):
            if v not in h:
                h[v]=len(h)+1
        return [h[i] for i in arr]
