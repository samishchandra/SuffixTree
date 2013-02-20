'''
Created on Oct 3, 2012

@author: KSC
'''
import sys;
import ShortestSuperString;

class Main():
    fileName = sys.argv[1] if (len(sys.argv) > 1) else 'sampleStrings.txt'
    inputStrings = [line.strip() for line in open(fileName)]

#    inputStrings = ['asdf', 'dfps', 'fpsas'];
    print(ShortestSuperString(inputStrings));
    

    
    
    
