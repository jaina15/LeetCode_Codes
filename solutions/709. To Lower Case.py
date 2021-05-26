class Solution:
    def toLowerCase(self, s: str) -> str:
        s1=''
        for i in s:
            if i >='A' and i <='Z':
                s1+=chr((ord(i)+32))
            else:
                s1+=i
            #print(s1)
        return s1
