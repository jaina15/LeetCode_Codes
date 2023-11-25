class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi = 0
        s=0
        for a in gain:
            s+=a
            maxi = max(s,maxi)
        return maxi
