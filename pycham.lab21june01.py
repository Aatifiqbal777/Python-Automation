# double
#
def double_me(a):
    return a * 2


my_list = [1, 2, 4, 3, 5, 6]


result = list(map(double_me, my_list))
print(result)

for i in result:
    print(i)
