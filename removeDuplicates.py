class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        k = 0
        for i in range(len(nums)):
            if not d.get(nums[i]):
                d[nums[i]] = 1
                nums[k] = nums[i]
                k += 1
        return k
