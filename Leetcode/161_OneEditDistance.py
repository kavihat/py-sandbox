class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False
        if s == t:
            return False

        if len(s) > len(t):
            lstr = s
            sstr = t
        else:
            lstr = t
            sstr = s
        i = j = 0
        count = 0
        flag = True
        while i < len(lstr) and j < len(sstr):
            if count > 1:
                flag = False
                break
            else:
                if lstr[i] == sstr[j]:
                    i += 1
                    j += 1
                else:
                    if len(lstr) == len(sstr):

                        count += 1
                        i += 1
                        j += 1
                    else:
                        count += 1
                        i += 1
        if count > 1:
            flag = False
        return flag


