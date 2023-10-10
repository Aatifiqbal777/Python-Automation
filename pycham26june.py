my_dict = {"name": "Alice", "age": 25}
print(my_dict)

# accessing values

print(my_dict["name"])

# updating values:
my_dict["age"] = 26
print(my_dict)

my_dict = {"name": "alice", "age": 25, "age": 26}
print(my_dict)
# no duplicat keys
# duplicat values is posible
my_dict["city"] = "new york"  # values adding is allowed
print(my_dict)

# deleting key-values pairs
del my_dict["age"]
del my_dict["city"]
print(my_dict)

# mixed dic
my_dict = {"name": "alice", "age": 25, "is male": "ture", "bal": 120}
print(my_dict)

# any keys use None, 12, name,c,---int,flot,str,bool,none,
my_dict1 = {'c': "Alice", 2: 33}
my_dict2 = {'None': "Alice", 2: 33}
my_dict3 = {'12': "Alice", 2: 33}
my_dict4 = {'ture': "Alice", 2: 33}
my_dict5 = {'l-student': [1, 2, 3, 4], 2: 33}
my_dict6 = {'t-student': [1, 2, 3, 4], 56: 33}

print(my_dict1, my_dict2, my_dict3, my_dict4, my_dict5, my_dict6)
print(my_dict6)

for key in my_dict:
    print(key)

print(my_dict["name"])

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
