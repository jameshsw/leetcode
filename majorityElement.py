class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        h = math.floor(n/2 + 0.5)
        print(f"{n}, {h}")
        for i in range(n):
            count = d.get(nums[i], 0) + 1
            if count >= h:
                return nums[i]
            d[nums[i]] = count
        return None
