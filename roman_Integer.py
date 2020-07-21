class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if s[i] == 'I':
                count = count + 1
            elif s[i] == 'V':
                if i != 0 and s[i - 1] == "I":
                    count = count + 3
                else:
                    count = count + 5
            elif s[i] == 'X':
                if i != 0 and s[i - 1] == 'I':
                    count = count + 8
                else:
                    count = count + 10
            elif s[i] == 'L':
                if i != 0 and s[i - 1] == 'X':
                    count = count + 30
                else:
                    count = count + 50
            elif s[i] == 'C':
                if i != 0 and s[i - 1] == 'X':
                    count = count + 80
                else:
                    count = count + 100
            elif s[i] == 'D':
                if i != 0 and s[i - 1] == 'C':
                    count = count + 300
                else:
                    count = count + 500
            elif s[i] == 'M':
                if i != 0 and s[i - 1] == 'C':
                    count = count + 800
                else:
                    count = count + 1000

        return count

s = Solution()
output=s.romanToInt(input('Enter a Roman Numeral: '))
print('Integer is: ',output)

