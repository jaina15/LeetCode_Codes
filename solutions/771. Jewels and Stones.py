class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = list(jewels)
        c=0
        for i in stones:
            if i in jewels:
                c+=1
        return c
                
