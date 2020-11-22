import re


class Solution:
    def numUniqueEmails(self, emails) -> int:
        count=0
        pattern1 = re.compile(r'[a-zA-Z]+[.]+[a-zA-Z]+@[a-zA-Z]+\.com$')
        pattern2= re.compile(r'[a-zA-Z]+[+]+[a-zA-Z]+@[a-zA-Z]+\.com$')
        pattern3=re.compile(r'[a-zA-Z]+[.+]+[a-zA-Z]+@[a-zA-Z]+\.com$')
        pattern4=re.compile(r'[a-zA-Z]+[a-zA-Z]+@[a-zA-Z]+\.com$')
        for i in emails:
            if not re.search(pattern3,i):
                return 0
            else:
                if re.search(pattern1,i) or re.search(pattern2,i) or re.search(pattern2,i) or re.search(pattern2,i):
                    count=count+1


