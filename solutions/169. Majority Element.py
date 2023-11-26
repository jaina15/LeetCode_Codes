class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Moore's voting algo
        el,cnt=0,0
        for i in nums:
            if cnt==0:
                el = i
                cnt+=1
            elif i==el:
                cnt+=1
            else:
                cnt-=1
        cnt1=0
        for i in nums:
            if i==el:
                cnt1+=1
        if cnt1>len(nums)/2:
            return el
        return -1
