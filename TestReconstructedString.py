'''
Created on Oct 3, 2012

@author: KSC
'''

import sys;
import random;
import ShortestSuperString;


class Main():
    inputString = sys.argv[1] if (len(sys.argv) > 1) else 'ABACADABRA'
    noOfFragments = int(sys.argv[2]) if (len(sys.argv) > 2) else 3
    fragmentLength = int(sys.argv[3]) if (len(sys.argv) > 3) else 5
    
    randomFragments = []
    for i in range(0, noOfFragments):
        fragmentIndex = random.randrange(0, len(inputString) - fragmentLength);
        randomFragment = inputString[fragmentIndex:(fragmentIndex + fragmentLength)];
        randomFragments.append(randomFragment)
    
    print(randomFragments);
    
    print(ShortestSuperString.ShortestSuperString(randomFragments));
    
