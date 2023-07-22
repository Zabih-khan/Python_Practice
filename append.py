# Python program to illustrate a list  
class list1:
    def create(self,nums):
        self.nums=nums
        self.nums.append(34) 
        self.nums.append(40.5) 
        self.nums.append("String") 
  
        print(self.nums) 

        
obj=list1()
nums = []
obj.create(nums)
