#!/usr/bin/env python3
import sys
key=int(sys.argv[1])
string=int(sys.argv[2])
if (len(sys.argv)== 3) and (key<string) :

        result = [x+1 for x in range(key-1 ,string)]

        print(result)

else:        
        
    print("none")