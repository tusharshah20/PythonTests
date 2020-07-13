
#Finding two numbers whose sum is x from a list
mylist = [1,2,3,4,9,7,11,8,13,19,20,18]
target = 38
class solution:
    def mid(self,list = [],target=0):
        list.sort()
        mid = int(len(list)/2)
        lele = len(list)
        t = list[mid]
        if target>mid:
            listN = list[t:lele]
            for i in listN:
                for j in listN:
                    if i+j==target:
                        return [list.index(i),list.index(j)]
                        
        else:
            listN = list[0:t]
            for i in listN:
                for j in listN:
                    if i+j==target:
                        return [list.index(i),list.index(j)]
                        
solution.mid(self="test",list = mylist,target=38)

#Finding two numbers whose sum is x from a list
class solution:
    from typing import List
    def twoSum(self,nums: List[int],target: int) -> List[int]:
        nums.sort()
        mid = int(len(nums)/2)
        lele = len(nums)
        t = nums[mid]
        if target>mid:
            numsx = nums[t:lele]
            newl = []
            for i in numsx:
                for j in numsx:
                    if i+j==target:
                        newl.append(nums.index(i))
                        newl.append(nums.index(j))
                        return newl
                        
        else:
            numsx = nums[0:t]
            newl = []
            for i in numsx:
                for j in numsx:
                    if i+j==target:
                        newl.append(nums.index(i))
                        newl.append(nums.index(j))
                        return newl

mylist = [1,2,3,4,9,7,11,8,13,19,19,20,18]
solution.twoSum(self="test",nums = mylist,target=38)