class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mcodes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans=set()
        for i in range(len(words)):
            s=''
            for j in words[i]:
                #print(ord(j)-97+1)
                s+=mcodes[ord(j)-97]
            #print(s)
            ans.add(s)
        return len(ans)
