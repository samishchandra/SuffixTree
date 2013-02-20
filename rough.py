'''
Created on Oct 1, 2012

@author: KSC
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    
    def findNonMatchingIndex(self, sampleString, startIndex, endIndex, sIndex, eIndex):
        i = 0;
        while i < (endIndex - startIndex):
            if(((sIndex + i) >= eIndex) or sampleString[startIndex + i] != sampleString[sIndex + i]):
                return i;
            i = i + 1;
        
        return endIndex;
    
    def myPrint(self, fun, param):
        fun(param);
        
    str1 = 'thisthxo';
    sIndex = 4;
    eIndex = 8;
    print(str1[sIndex:eIndex]);
    
    print(findNonMatchingIndex(0, str1, 0, len(str1), sIndex, eIndex));
#    print(str1[0:findNonMatchingIndex(0, str1, 0, len(str1), sIndex, eIndex)]);
    myPrint(0, print, 'asdf');
    
   
