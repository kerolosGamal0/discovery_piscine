#!/usr/bin/env python3
import sys

if len(sys.argv)<2:
    print("none")
else:
   l=len(sys.argv) - 1
   print(f"parameters: {l}")
 
   for x in  sys.argv[1:]:
      print(f"{x}",len(x))