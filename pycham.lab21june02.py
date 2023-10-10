def saquare_me(a):
    return pow(2, a)


numbers = [2, 3, 4, 6]
result = map(saquare_me, numbers)
print(result)
print(type(result))
result = list(result)
print(result)

# use of filter
my_list = [67, 78, 98]
max_result = max(my_list)
print(max_result)

sort_result = sorted(my_list)
print(sort_result[len(sort_result) - 1])
