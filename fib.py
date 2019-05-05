# 斐波那契数列,100以内
# a = 0
# b = 1
# while True:
#     c = a+b
#     a, b = b, c
#     if c>100:
#         break
#     print(c)


# 斐波那契数列前100项
# a = 0
# b = 1
# numb = 0
# while True:
#     c = a + b
#     a,b = b,c
#     numb += 1
#     print(c)
#     if numb>=10:
#         break


# lst = ['1','2','3']
# print('..'.join(lst))

# split将字符串按照分隔符分割成若干字符串，返回列表，去掉了分隔符，缺省的时候空白字符作为分隔符
# a = 'a b cd efg'
# b = a.split('c')
# print(b)

# partition将字符串按照分隔符分割成前一段，分隔符，后一段的元组，必须指定分隔符
# a = 'aa_aa adf_a'
# b = a.partition('_')
# print(b)


# strip从字符串两端去除指定的字符集中的所有字符，如果没有指定去除两端的空白字符
# a = 'abcadbe'
# b = a.strip('ae')
# print(b)

# 斐波那契

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a , b = b, a+b
    return b

print(fib(6))















