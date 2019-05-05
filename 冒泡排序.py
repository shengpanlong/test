#冒泡法
#两两比较大小，交换位置
#升序，n个数从左至右，编号从0到n-1，索引0和索引1进行比较，如果索引0大，则两者交换位置，如果索引1大，则不交换，继续比较索引1和索引2，将大值放在右侧，依次类推，第一轮比较完
#则最大值在最右侧，第二轮比较0到n-2，依次类推
#降序与升序相反

num = [1,2,0,3,2,123,32,45]
l = len(num)
for j in range(l):
    flag = False
    for i in range(l-j-1):
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
            flag = True
    if not flag:
        break
print(num)



