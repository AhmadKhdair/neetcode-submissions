class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        threshold=len(nums)/2
        for i in range(len(nums)):
            if nums[i] not in d.keys():
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
            if d[nums[i]] >=threshold:
                return nums[i]