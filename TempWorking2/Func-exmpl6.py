from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                    index_map = {}
                    for i in range(len(nums)):
                        num = nums[i]
                        pair = target - num
                        if pair in index_map:
                            return [index_map[pair], i]
                        index_map[num] = i
                    return None
Solution.twoSum("Test",nums=[0,1,6],target=6)
