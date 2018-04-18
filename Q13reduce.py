import functools

my_list = [3,5,2,11,6,8]
a=functools.reduce(lambda x, y: x*y, my_list)
print(a)


