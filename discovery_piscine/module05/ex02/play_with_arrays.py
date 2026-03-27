#!/usr/bin/env python3

my_list = [2, 8, 9, 48, 8, 22, -12, 2]
mod_list=[]
for i in range(len(my_list)):
    if my_list[i]>5:
        mod_list.append(my_list[i])
          
new_list=[x+2 for x in mod_list]

print(f"Original array: {my_list}")
print(f"New array:{new_list}")