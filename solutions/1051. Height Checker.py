class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt=0
        for nums in zip(heights,sorted(heights)):
            if nums[0]!=nums[1]:
                cnt+=1
        return cnt
