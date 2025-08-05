class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        k = 0
        for i in range(0, len(nums)):
            count = d.get(nums[i], 0)
            if count < 2:
                nums[k] = nums[i]
                d[nums[i]] = count + 1
                k += 1
        return k
                
            
