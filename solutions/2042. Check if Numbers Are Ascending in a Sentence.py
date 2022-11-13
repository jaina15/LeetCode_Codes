class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev=-1
        s=s.split()
        for char in s:
            if char.isnumeric():
                if int(char)<=prev:
                    return False
                else:
                    prev=int(char)
        return True
