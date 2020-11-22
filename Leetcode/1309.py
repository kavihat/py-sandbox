class Solution:
    def freqAlphabets(self, s: str) -> str:

        print(s)
        output=''
        i=0
        while i <len(s):
            if i<len(s)-2 and s[i+2]=='#':
                output=output+chr(int(s[i]+s[i+1])+96)
                i=i+3

            else:
                output=output+chr(int(s[i])+96)
                i=i+1

        return output

s=Solution()
final=s.freqAlphabets('10#11#1')
print(final)

