class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l=[0]*(len(gain)+1)
        print(len(l))
        for i in range(len(gain)):
            l[i+1]=l[i]+gain[i]
        return max(l)
