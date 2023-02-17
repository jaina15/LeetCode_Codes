class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran,mag=dict(),dict()
        for i in ransomNote:
            if i in ran:
                ran[i]+=1
            else:
                ran[i]=1
        for i in magazine:
            if i in mag:
                mag[i]+=1
            else:
                mag[i]=1
        for k,v in ran.items():
            if k not in mag:
                return False
            elif ran[k]>mag[k]:
                return False
        return True
