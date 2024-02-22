class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c=0
        if digits[-1]<9:
            digits[-1]+=1
            return digits
        elif digits[-1]==9:
            l=len(digits)-1
            c=1
            while l>-1 and c:
                digits[l]+=1
                c=digits[l]//10
                digits[l]%=10
                l-=1
            if c:
                digits.insert(0,c)
        return digits
