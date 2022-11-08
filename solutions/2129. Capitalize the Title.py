class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        for i,v in enumerate(words):
            if len(v)>2:
                words[i]=v.capitalize()
            else:
                words[i]=v.lower()
        return ' '.join(words)
