class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        l = [nums[0],nums[0]]
        for i in range(1, len(nums)):
            if nums[i] - l[1] == 1:
                l[1] = nums[i]
            else:
                if l[0] == l[1]:
                    res.append(f"{l[0]}")
                else:
                    res.append(f"{l[0]}->{l[1]}")
                l = [nums[i],nums[i]]

        if l[0] == l[1]:
            res.append(f"{l[0]}")
        else:
            res.append(f"{l[0]}->{l[1]}")
        return res

        """
        if not nums:
            return []
        res = []
        l = []
        for i in nums:
            if not l:
                l = [i,i]
            else:
                if i - l[1] == 1:
                    l[1] = i
                else:
                    if l[0] == l[1]:
                        res.append(str(l[0]))
                    else:
                        res.append(str(l[0])+"->"+str(l[1]))
                    l = [i,i]
            if i == nums[-1]:
                if l[0] == l[1]:
                    res.append(str(l[0]))
                else:
                    res.append(str(l[0])+"->"+str(l[1]))
        return res
        """
