class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch in '[{(':
                st.append(ch)
            else:
                if len(st) == 0: return False
                if ch == ')':
                    if st[-1] != '(': return False
                    else: st.pop()
                elif ch == '}':
                    if st[-1] != '{': return False
                    else: st.pop()
                elif ch == ']':
                    if st[-1] != '[': return False
                    else: st.pop()
        return True if len(st) == 0 else False
                

        