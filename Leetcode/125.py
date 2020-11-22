"""
1125. Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        flag=1
        j=len(s)-1
        while i<=j:
            if s[i].isalnum():
                if s[j].isalnum():
                    if s[i].lower()==s[j].lower():
                        i=i+1
                        j=j-1
                    else:
                        flag=0
                        break
                else:
                    j=j-1
            else:
                i=i+1
        if flag==1:
            return True
        else:
            return False

s=Solution()
output=s.isPalindrome('0P')
print(output)
