def bin_add(num1, num2, carry):


    final = []
    for i in reversed(range(len(num1))):

        # if num1[i]==0 and num2[i]==0:
        #      print(num1[i])
        print('inside loop')
        print(num1[i], num2[i], carry)
        if num1[i] == '0' and num2[i] == '0' and carry == '0':
            value = '0'
            carry = '0'
        elif num1[i] == '0' and num2[i] == '0' and carry == '1':
            value = '1'
            carry = '0'
        elif num1[i] == '0' and num2[i] == '1' and carry == '0':
            value = '1'
            carry = '0'
        elif num1[i] == '0' and num2[i] == '1' and carry == '1':
            value = '1'
            carry = '1'
        elif (num1[i] == '0' and num2[i] == '1' and carry == '1') or (
                num1[i] == '1' and num2[i] == '0' and carry == '1'):
            value = '0'
            carry = '1'
        elif (num1[i] == '0' and num2[i] == '1' and carry == '0') or (
                num1[i] == '1' and num2[i] == '0' and carry == '0'):
            print("second")
            print('here')
            value = '1'
            carry = '0'
        elif (num1[i]=='1' and num2[i]=='1' and carry=='1'):
            value='1'
            carry='1'
        elif (num1[i]=='1' and num2[i]=='1' and carry=='0'):
            value='0'
            carry='1'
        final.insert(0, value)

    return final


# bin1 = list(input("Enter first num"))
# bin2 = list(input('Enter second num'))
# print(bin1)
bin1 = ['1', '0', '1', '1', '0', '1']
bin2 = ['1', '1', '1', '1', '0', '1']

carry = '0'
result = bin_add(bin1, bin2, carry)
print("result is ", result)
