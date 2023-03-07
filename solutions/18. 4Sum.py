class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                tsum=target-(nums[i]+nums[j])
                lo=j+1
                hi=len(nums)-1
                while lo<hi:
                    if tsum==nums[lo]+nums[hi]:
                        ans.append([nums[i],nums[j],nums[lo],nums[hi]])
                        while lo<hi and nums[lo]==nums[lo+1]:
                            lo+=1
                        while lo<hi and nums[hi]==nums[hi-1]:
                            hi-=1
                        lo+=1
                        hi-=1
                    elif tsum>nums[lo]+nums[hi]:
                        lo+=1
                    else:
                        hi-=1
        return ans
