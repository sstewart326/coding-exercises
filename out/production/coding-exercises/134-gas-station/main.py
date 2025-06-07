from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) + sum(cost) < 0:
            return -1
        else:
            start_idx = 0
            remaining_gas = 0

            for i in range(len(gas)):
                curr_cost = gas[i] - cost[i]
                if curr_cost + remaining_gas < 0:
                    start_idx = i + 1
                    remaining_gas = 0
                else:
                    remaining_gas += curr_cost

            return start_idx


def main():
    sol = Solution()
    print(sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))

if __name__ == "__main__":
    main()