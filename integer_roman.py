class Solution:
    def intToRoman(self, num: int) -> str:
        rdict={1:'I',2:'X',3:'C',4:'M'}
        ldict={1:'V',2:'L',3:'D'}
        output=''
        count=1
        while num:
            first_digit = num % 10

            if first_digit>0 and first_digit<4:
                output=first_digit*rdict[count]+output
            elif first_digit==4:
                output=rdict[count]+ldict[count]+output
                # return output
            elif first_digit>4 and first_digit<9:
                output=ldict[count]+(first_digit-5)*rdict[count]+output
                # return output
            elif first_digit == 9:
                output = rdict[count]+rdict[count+1]+output
                # return output
            elif first_digit==0:
                pass

            num = int(num / 10)
            count=count+1
        return output






s=Solution()
output=s.intToRoman(int(input('Enter an integer: ')))
print('Roman Numeral is: ',output)