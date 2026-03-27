#!/usr/bin/env python3

def array_of_names (x):
    f_names=[]
    for first , last in x.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        f_names.append(full_name)
    return f_names




persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))