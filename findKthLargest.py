class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
        """
        heapq.heapify(nums)
        kth = None
        for _ in range(k+1):
            kth = heapq.heappop(nums)
        return kth
        """

        
