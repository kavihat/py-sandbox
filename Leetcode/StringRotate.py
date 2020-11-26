class Solution:
    def rotateString(self, inp: str, rotated: str) -> bool:
        if len(inp)!=len(rotated):
            return False
        i=0
        k=0
        res=[]
        tracker=-1
        while i<len(rotated):
            if rotated[i]==inp[k]:
                res.append(rotated[i])
                i+=1
                k+=1
            else:
                i=i-(len(res)-1)
                res=[]
                k=0

        return ''.join(res)+rotated[:len(inp)-len(res)] == inp
