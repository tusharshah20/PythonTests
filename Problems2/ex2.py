# # import collections
# # l = ["he","she","he","she","he"]
# # print(sorted(collections.Counter(l)))
# # def twoSum(self, nums: List[int], target: int) \
# #   -> List[int]:
  
        
# # class this_is_class:
# #   def show(in_place_of_self):
# #     print("we are using this in place of self")
# # object = this_is_class()
# # object.show()

# class car:
#   def __init__(self,model,color):
#     self.model = model
#     self.color = color
#   def show(self):
#     print("model of car is: ",self.model)
#     print("color of car is: ",self.color)
# audi = car("newModel","blue")
# merc = car("newModel","red")

# audi.show()
# merc.show()

#Problem:
'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.'''
#Solution1:
class Solution:
    def twoSum(self,nums = [],target: int = 0) -> []:
        newl = []
        for i in nums:
            for j in nums:
                if i+j==target:
                    print("numbers are: " + \
                        str(i) + " and " + str(j))
                    [print(nums.index(i),nums.index(j))]
                    newl.append(nums.index(i))
                    newl.append(nums.index(j))
                    return newl
Solution.twoSum(self="test",nums = [2,7,11,15],target=9)