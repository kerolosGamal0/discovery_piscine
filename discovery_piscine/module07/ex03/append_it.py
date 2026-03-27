#!/usr/bin/env python3
import sys
l=len(sys.argv)
count=sys.argv
if l == 1:
    print("none")
else:


  for x in range (l) :
    if count[x].endswith("ism"):
        continue
    else:
        print(f"{count[x]}ism")
    
