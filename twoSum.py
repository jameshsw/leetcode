class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in seen:
                return [i, seen[remainder]]
            seen[num] = i
        """
        sorted_nums = sorted(enumerate(nums), key=lambda x:x[1])
        nums_len = len(nums)
        l = 0
        r = nums_len-1
        while r > l:
            tot = sorted_nums[l][1] + sorted_nums[r][1]
            if tot == target:
                return [sorted_nums[l][0],sorted_nums[r][0]]
            if tot > target:
                r -= 1
            else:
                l += 1
        """
        
