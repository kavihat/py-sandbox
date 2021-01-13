class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        invalid_index = set()
        result = []
        for i in range(len(s)):

            if s[i] == '(':
                stk.append(i)
            elif s[i] == ')' and len(stk) > 0:
                stk.pop()
            elif s[i] == ')' and len(stk) == 0:
                invalid_index.add(i)

        while stk:
            index = stk.pop()
            invalid_index.add(index)

        for i in range(len(s)):
            if i not in invalid_index:
                result.append(s[i])
        return "".join(result)