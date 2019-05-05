

# 降序
# 在未排序序列中，构建一个子排序序列，直到全部数据排序完成
# 将待排序的数，插入到已经排序的序列中的合适位置
# 增加一个哨兵，放入待比较的值，让它和后面已经排好序的序列比较，找到合适的插入点

nums = [9] + [1,3,4,6,3,2,6,8]
print(nums)
length = len(nums)
for i in range(2,length):
    nums[0] = nums[i]
    j = i-1
    if nums[j]<nums[0]:
        while nums[j]<nums[0]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = nums[0]
print(nums)
