#!/usr/bin/env python3
import sys

def shrink(s):
     print(s[:8])


def enlarge(s):
    print(s.ljust(8, 'Z'))
if len(sys.argv)==1:
     print("none")

for arg in sys.argv[1:]:
        length = len(arg)
        if length > 8:
            shrink(arg)
        elif length < 8:
            enlarge(arg)
        else:
            print(arg)