class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        n = len(nums)
        bucket = [0] * (n + 1)
        for num, freq in counter.items():
            if bucket[freq] == 0:
                bucket[freq] = [num]
            else:
                bucket[freq].append(num)
        res = []
        idx = n
        while k > 0:
            if bucket[n] != 0:
                res.extend(bucket[n])
                k -= len(bucket[n])
            n -= 1
        return res
