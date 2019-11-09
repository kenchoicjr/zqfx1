# import random
#
# print(random.randint(0, 9))
#
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(nums.remove(0))
# for a in nums:
#     for b in nums.pop(0):
#         print(b)

list1 = [0,1,2,3,4,5,6,7,8,9]
for a in list1:
    print(a)
    list2 = list1.remove(a)
    print(list2)