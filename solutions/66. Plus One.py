class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=[str(digits) for digits in digits]
        #print(s)
        s="".join(s)
        n=int(s)
        #print(n)
        n+=1;
        digits.clear()
        #print(digits)
        while n>0:
            digits.append(n%10)
            n=n//10
        
        digits.reverse()
        return digits
