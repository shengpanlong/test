#选择排序
#两两比较大小，找出极大值或极小值被放置在固定位置，这个固定位置一般指的是某一端
#降序，n个数从左至右，索引从0到n-1，两两依次比较，记录大值索引，此轮所有数比较完毕
#将大数和索引0交换，如果大数就是索引0，不交换.第二轮，从1开始比较，找到最大值，将它和索引1位置交换
#如果它就是索引1位置则不交换，依次类推，每次左边都会固定下一个大数
#升序与降序相反
#时间复杂度O(n**2)

num = [78,3,23,4,5,0]
l = len(num)
for i in range(l):
    maxindex = i
    for j in range(i+1,l):
        if num[maxindex] < num[j]:
            maxindex = j
    if i != maxindex:
        num[i], num[maxindex] = num[maxindex], num[i]

print(num)
