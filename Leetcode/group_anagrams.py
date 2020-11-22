class Solution:
    def groupAnagrams(self, strs):
        dct = {}
        res = []
        for element in strs:
            temp = tuple(sorted(list(element)))
            if temp in dct:
                dct[temp].append(element)
                print(element)
            else:
                dct[temp] = [element]
        for item in dct:
            res.append(dct[item])
        return res


s=Solution()
out=s.groupAnagrams(["a"])
print(out)


