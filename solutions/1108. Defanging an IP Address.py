class Solution:
    def defangIPaddr(self, address: str) -> str:
        l=list(address)
        #print(l)
        for n,i in enumerate(l):
            if i=='.':
                l[n]='[.]'
        #l=l.replace('.','[.]')
        address=''.join(l)
        #print(address)
        return address
