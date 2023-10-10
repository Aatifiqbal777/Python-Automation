# list use []
# sotre of element
# different data types
# list itmes are changeble

# create a list
my_marks = []
my_marks2 = list
print(type(my_marks))

# use of insert
my_marks.insert(0, 9)
my_marks.insert(1, 97)
my_marks.insert(1, 77)
print(my_marks)

# use of append
my_marks.append(86)
print(my_marks)
print(len(my_marks))

# use of remove
my_marks.remove(77)
print(my_marks)

# nested_list use
nested_list = [[1, 2, 3], [5, 6, 7], [0, 7, 5]]
print(nested_list[0])
print(nested_list[2])
print(nested_list[1])

nested_list[0] = ["qab", "sab", "hgf"]
print(nested_list)

# use of duplicat_list
dup_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(dup_list)

# use of mixture-list
mix_list = ["apple", 123, True]
print(mix_list)

#create range
sq = [i**2 for i in range(10)]
print(sq)

num = list(range(1,20))
print(num)

# list built in function

my_list = [1,2,3]
print(my_list[0])
print(my_list[0:1])
print(my_list[0:2])
print(my_list[:-1])

# extend
my_list.extend([4,5,6,7])
print(my_list)

#pop ; remove an item
i= my_list.pop(1)
print(i)
print(my_list)

my_list.append(5)
print(my_list)

#count use
print(my_list.count(5))

my_list.reverse()
print(my_list)