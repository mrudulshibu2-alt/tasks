nums = [10,20,30,40,50]
# nums[1]=100
print(nums)

nums.append(1000)
print(nums)

nums.insert(1,100)
print(nums)

#extend
nums.extend([200,300])
print(nums)

#to remove
nums.remove(50)
print(nums)
nums.pop()
print(nums)

#delete
del nums[0]
print(nums)

nums.clear()
print(nums)