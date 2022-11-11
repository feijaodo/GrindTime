class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for n,num in enumerate(nums):
            if target-num in d:
                return d[target-num],n
            else:
                d[num]=n
                    