class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ = len(nums)*(len(nums)+1)//2
        return summ-sum(nums)
        
        # can be done with XOR as well
        # take xor for 1 to len(nums)
        # take xor of all array elements
        # return xor of above 2
