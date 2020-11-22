class Solution:
    def firstUniqChar(self, s: str) -> int:
        # output = 0
        # if s=='':
        #     return -1
        # for i in range(len(s)):
        #     if s.count(s[i])>1:
        #         i=i+1
        #     else:
        #         return i
        # return -1
        minimum_index=0
        m_dict={}
        for i in range(len(s)):

            if s[i] in m_dict:
                m_dict[s[i]] = [i, m_dict[s[i]][1] +1]
            else:
                m_dict.update({s[i]:[i,1]})
        min =len(s)
        flag=0
        for k in m_dict:

            if m_dict[k][1]==1:
                flag=1
                if m_dict[k][0]<min:
                    min=m_dict[k][0]

            else:
                continue
        if min==len(s):
            return -1
        else:
            return min


s=Solution()
final=s.firstUniqChar("")
print(final)
