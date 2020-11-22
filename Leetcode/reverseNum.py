class Solution:
    def reverse(self, x: int) -> int:
        output=0
        if x<0:
            flag=0
            x=-1*x
        else:
            flag=1
        while x:
            digit=x%10
            output=output*10+digit
            x=int(x/10)
        if output in  [-2^31,2^31-1]:
            return 0
        elif flag==0:
            return -1*output
        else:
            return output

s=Solution()
final=s.reverse(-123)
print(final)

