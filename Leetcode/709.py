"""
To Lower Case
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
"""


class Solution:
    def toLowerCase(self, str) -> str:
        lower=''
        for i in str:
            if ord(i) >=65 and ord(i)<=90:
                lower=lower+(chr(ord(i)+32))
            else:
                lower=lower+i


        return lower

s=Solution()
out=s.toLowerCase('HelloHH')
print(out)
