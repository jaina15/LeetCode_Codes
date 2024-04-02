class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack,t_stack=[],[]
        for c in s:
            if c=='#' and s_stack:
                s_stack.pop()
            else:
                if c!='#':
                    s_stack.append(c)
        for c in t:
            if c=='#' and t_stack:
                t_stack.pop()
            else:
                if c!='#':
                    t_stack.append(c)
        return ''.join(s_stack)==''.join(t_stack)
