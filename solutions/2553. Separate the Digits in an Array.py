class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for n in nums:
            l=[]
            while n>0:
                l.append(n%10)
                n//=10
            ans.extend(l[::-1])
        return ans
