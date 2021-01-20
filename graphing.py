import matplotlib.pyplot as plt

with open('assembly.txt', 'r+') as f:
    nums = [int(x) for x in f]
    x = [x+1 for x in range(len(nums))]
    '''
with open('assembly2.txt', 'r+') as f:
    nums2 = [int(x2) for x2 in f]
    x2 = [x2+1 for x2 in range(len(nums2))]
'''
with open('assembly3.txt', 'r+') as f:
    nums3 = [int(x3) for x3 in f]
    x3 = [x3+1 for x3 in range(len(nums3))]
fig=plt.figure()
plt.scatter(x, nums, c='b', label='one')
#plt.scatter(x2, nums2, c='r', label='three')
plt.scatter(x3, nums3, c='g', label='three')
plt.legend(loc='upper left')
plt.show()

