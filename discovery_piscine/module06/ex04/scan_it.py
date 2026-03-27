#!/usr/bin/env python3
import re
import sys
if len(sys.argv)== 3:
        key=sys.argv[1]
        string=sys.argv[2]

        result = re.findall(key, string)

        print(len(result))

else:        
        
    print("none")
