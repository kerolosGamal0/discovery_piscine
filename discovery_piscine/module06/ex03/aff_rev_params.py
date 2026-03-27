#!/usr/bin/env python3
import sys

if len(sys.argv)<3:
    print("none")
else:
 for x in reversed(sys.argv):
    print(x)