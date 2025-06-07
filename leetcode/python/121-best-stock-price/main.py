from typing import List


# Input [4,1,5,2,7]
# Output 6
# - two pointers
# - max profit
# - lowest price
# - curr - low_price to get current_profit
# - j pointer increments each time
# - i pointer increments each time we find a lowest_price
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        lowest_price = prices[0]
        max_profit = 0

        # [4, 1, 5, 2, 7]
        #     ^        ^

        for price in prices:
            max_profit = max(max_profit, price - lowest_price)
            lowest_price = min(lowest_price, price)

        return max_profit


def main():
    sol = Solution()
    prices = [4, 1, 5, 2, 7]
    print(sol.maxProfit(prices)) #6
    prices = [4, 3, 5, 2, 7]
    print(sol.maxProfit(prices)) #5

if __name__ == "__main__":
    main()