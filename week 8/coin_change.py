class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = 0
        dp = set()
        dp.add(amount)
        while True:
            new_dp = set()
            for ele in dp:
                if ele == 0:
                    return res
                for coin in coins:
                    diff = ele - coin
                    if diff >= 0 and diff not in new_dp and diff not in dp:
                        new_dp.add(diff)
            res += 1
            if len(new_dp) == 0:
                return -1
            dp = new_dp