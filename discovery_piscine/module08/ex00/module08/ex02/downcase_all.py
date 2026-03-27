#!/usr/bin/env python3
import sys

def downcase_it(name ):
    return name.lower()


if len(sys.argv)<2:
    print("none")
else:
    l = len(sys.argv)
    for x in range (1,l):
       print(downcase_it(sys.argv[x]))