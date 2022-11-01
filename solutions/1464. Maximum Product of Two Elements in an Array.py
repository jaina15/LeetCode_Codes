class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1=max2=float('-inf')
        for i in nums:
            if i>=max1:
                max1,max2=i,max1
            elif i>max2:
                max2=i
        return (max1-1)*(max2-1)
