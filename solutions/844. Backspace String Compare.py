class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss,ts=[],[]
        for i in s:
            if i == '#':
                if len(ss)>0:
                    ss.pop()
            else:
                ss.append(i)
        for i in t:
            if i == '#':
                if len(ts)>0:
                    ts.pop()
            else:
                ts.append(i)
        return ss==ts
