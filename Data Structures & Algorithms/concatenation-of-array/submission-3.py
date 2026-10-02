class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length=len(nums)
        arr=[0]*length*2
        for x in range(length):
            arr[x]=nums[x]
            arr[(x+length)]=nums[x]
        return arr
     