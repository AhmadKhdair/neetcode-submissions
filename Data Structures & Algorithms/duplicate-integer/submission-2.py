class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen =set()
        for x in nums:
            seen.add(x)
        return len(seen)!=len(nums)