class Solution:
    def check(self, nums: List[int]) -> bool:
        l=sorted(nums)
        sl =''
        for i in l:
            sl+=str(i)+' '
        os=''
        for i in (nums+nums):
            os+=str(i)+' '
        return True if sl in os else False
