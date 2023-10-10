class employees:
    no_of_leves = 8
    pass
harry=employees()
larry=employees()
harry.name = "Aatif"
harry.salary = 234
harry.company ="amzon"
larry.name = "iqbal"
larry.salary = 547
larry.company = "dilote"

print(harry.company, larry.salary)
print(larry.no_of_leves)
print(harry.__dict__)
harry.no_of_leves =10
print(harry.__dict__)
print(larry.__dict__, harry.__dict__)



