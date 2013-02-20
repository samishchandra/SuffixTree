'''
Created on Oct 2, 2012

@author: KSC
'''

import SuffixTree;

def ShortestSuperString(inputStrings):
        
    if(inputStrings and len(inputStrings) <= 1): return inputStrings[0];
    
    str1 = inputStrings.pop();
    tree = SuffixTree.SuffixTree(str1);
    maxOverlapLength = 0;
    maxOverlapStringIndex = 0;
    for index in range(len(inputStrings)):
        overlapLength = tree.MaxOverlap(inputStrings[index]);
        if(maxOverlapLength <= overlapLength):
            maxOverlapLength = overlapLength;
            maxOverlapStringIndex = index;
    
    inputStrings[maxOverlapStringIndex] = str1 + inputStrings[maxOverlapStringIndex][maxOverlapLength:];
    print(inputStrings);
    return ShortestSuperString(inputStrings);



 
        
