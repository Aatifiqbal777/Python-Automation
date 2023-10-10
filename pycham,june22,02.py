# Tuple ()
car = ("i10", "safari", "i20", "ford")
print(car)
print(car[0])
print(car[1])
print(car[2])
print(car[0:2])
print(car[0:-1])
print(len(car))
print(car[3:0])
print(car[::-1])

# creating a tuple with
# use of list

list1 = [1, 2, 3, 4, 5, 6]
print("\ntuple using list: ")
print(tuple(list1))

list2 = tuple('Aatif iqbal')
print("\ntuple with the use of function")
print(list2)

# unpack
list = (3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,)
a, d, r, e, w, q, g, j, k, l, c, a, c, z = list
print(z)

print(list)
