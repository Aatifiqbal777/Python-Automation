# how to check if a list empty in python.(if len(lis1)==0)

my_list = []
non_list = [2, 3, 4]

isEmpty = len(my_list)
isEmpty = len(non_list)
if isEmpty == 0:
    print("list is Empty")
else:
    print("list is non empty")

# woh remove duplicat list


my_list = (33, 34, 45, 33, 43,)
non_dup = []

for i in my_list:
    if i not in non_dup:
        non_dup.append(i)
print(non_dup)

# check if two list are identical.

lis1 = [2, 4, 4]
lis2 = [2, 4, 8]
if lis1 == lis2:
    print("identical")
else:
    print("non_identical")
