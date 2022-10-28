class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        i,j=0,len(s)-1
        i_vowel,j_vowel=0,0
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        while i<j:
            if s[i] not in vowels:
                i+=1
            else:
                i_vowel=1
            if s[j] not in vowels:
                j-=1
            else:
                j_vowel=1
            
            if i_vowel and j_vowel:
                t=s[i]
                s[i]=s[j]
                s[j]=t
                
                i+=1
                j-=1
                
                i_vowel,j_vowel=0,0
        
        return ''.join(s)
