class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        open_b = {'(','{','['}
        hm = {')':'(','}':'{',']':'['}
        # close_b = set([')','}',']'])
        for i in s:
            if i in open_b:
                st.append(i)
            else:
                if not st:
                    return False
                top = st.pop()
                if top != hm[i]:
                    return False
        if st:
            return False
        return True
