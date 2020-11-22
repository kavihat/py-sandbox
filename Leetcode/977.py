# # squares of a sorted array
# class Solution:
#     def sortedSquares(self, A: list[int]) -> list[int]:
#         sqaured_numbers = [num ** 2 for num in A]
#         return sorted(sqaured_numbers)


# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
#         if word.islower():
#             return True
#         elif word.isupper():
#             return True
#         elif word==word.capitalize():
#             return True
#         else:
#             return False
#
# s=Solution()
# output=s.detectCapitalUse("lag")
# print(output)

#322

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        res=0
        count=0
        final=amount
        coins.sort(reverse=True)
        if amount==0:
            return 0
        if res<amount:
            for i in range(len(coins)):
                amount=amount-res
                if final<min(coins):
                    return -1
                elif amount%coins[i]==coins[i]:
                     i=i+1
                     break

                else:
                    q=int(amount/coins[i])
                    count=count+q
                    res=q*coins[i]
                    if amount-res == 1 and 1 not in coins:


                        return -1

            flag=1
        else:
            flag=0
        if flag==1:
            return count
        else:
            print('here')
            return -1

            # class Solution:
            #     def coinChange(self, coins: List[int], amount: int) -> int:
            #         dp = [float('inf')] * (amount + 1)
            #         dp[0] = 0
            #
            #         for coin in coi
            #         ns:
            #             for x in range(coin, amount + 1):
            #                 dp[x] = min(dp[x], dp[x - coin] + 1)
            #         return dp[amount] if dp[amount] != float('inf') else -1
            # return -1



s=Solution()
output=s.coinChange([186,419,83,408],6249)
print(output)















