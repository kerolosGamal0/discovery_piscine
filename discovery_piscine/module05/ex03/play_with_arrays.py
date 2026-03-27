#!/usr/bin/env python3
my_list=[2, 8, 9, 48, 8, 22, -12, 2]
my_set=set()
for x in range(len(my_list)):
    my_set.add(my_list[x])
print(f"{my_list}\n{my_set}")