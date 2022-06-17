class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j=set(jewels)
        c=0
        for i in stones:
            if i in j:
                c+=1
        return c
