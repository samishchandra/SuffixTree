'''
Created on Oct 1, 2012

@author: KSC
'''

class TreeNode(object):
    
    def __init__(self, level = 0, startIndex = None, endIndex = None, children = None):
        self.startIndex = startIndex; #startIndex in the original string
        self.endIndex = endIndex; #endIndex in the original string
        self.level = level; #to determine the level of the node from the root
        self.children = children or []; #children of the node
    
    def _setIndices(self, startIndex, endIndex):
        self.startIndex = startIndex;
        self.endIndex = endIndex;
    
    def IsLeaf(self):
        if(self.children): return False;
        else: return True;
            

class SuffixTree(object):

    def __init__(self, inputStr, specialChar = '$'):
        '''
        Constructor for Suffix Tree taking a string input
        '''
        self.rootNode = TreeNode();
        self.baseString = inputStr + specialChar;
        self.specialChar = specialChar;
        self._buildSuffixTree();

    def _buildSuffixTree(self):
        if(len(self.baseString) <= 0): return;
        
        length = len(self.baseString);
        for i in range(length):
#            print('Inserting string \"', self.baseString[i:length], '\"')
            self._insertString(self.rootNode, i, length)
    
    def _insertString(self, parentNode, startIndex, endIndex):
        if(startIndex >= endIndex): return;
        
        if(parentNode.IsLeaf()):
            parentNode.children.append(TreeNode(parentNode.level + 1, startIndex, endIndex, None));
#            print('inserted ', self.baseString[startIndex:endIndex], startIndex, endIndex)
            return;
        else:
            for child in parentNode.children:
                findNonMatchingIndex = self._findNonMatchingIndex(child, startIndex, endIndex)
#                print(self._nodeFString(child), 'findNonMatchingIndex', findNonMatchingIndex);
                if(findNonMatchingIndex == child.endIndex):
                    self._insertString(child, findNonMatchingIndex - child.startIndex + startIndex, endIndex);
                    return;
                elif(findNonMatchingIndex > child.startIndex):
#                    print('node for branching', self._nodeFString(child));
                    newBranchNode = TreeNode(child.level + 1, findNonMatchingIndex, child.endIndex, child.children)
                    child.endIndex = findNonMatchingIndex;
                    child.children = []
#                    print('node after branching', self._nodeFString(child));
#                    print('branched node', self._nodeFString(newBranchNode));
                    child.children.append(newBranchNode)
                    if((endIndex - (findNonMatchingIndex - child.startIndex + startIndex)) > 0):
#                        print(str(endIndex) + ' ' + str(findNonMatchingIndex));
#                        print('created child', self._nodeFString(TreeNode(findNonMatchingIndex, endIndex)));
                        child.children.append(TreeNode(child.level + 1, findNonMatchingIndex - child.startIndex + startIndex, endIndex, None));
                    return;
            
#            print('created new child', self.baseString[startIndex:endIndex]);
            parentNode.children.append(TreeNode(parentNode.level + 1, startIndex, endIndex, None));
            return;
    
    def _findNonMatchingIndex(self, node, startIndex, endIndex):
        i = 0;
        while i < (node.endIndex - node.startIndex):
            if(((startIndex + i) >= endIndex) or self.baseString[node.startIndex + i] != self.baseString[startIndex + i]):
                return (node.startIndex + i);
            i = i + 1;
        
        return node.endIndex;
    
    def PrintSuffixes(self):
        self._printSuffixes('', self.rootNode);
    
    def _printSuffixes(self, suffixString, node):
        if(node.IsLeaf()):
            print(suffixString + self._nodeString(node));
            return;
        
        for child in node.children:
#            print("child: ", self._nodeFString(child), node.startIndex);
            self._printSuffixes(self._nodeString(node) + suffixString, child);
    
    def _nodeString(self, node):
        if(node.startIndex is not None):
            return self.baseString[node.startIndex:node.endIndex];
        else:
            return '';
    
    def _nodeFString(self, node):
        if(node.startIndex is not None):
            return ('Node: (' + str(node.startIndex) + ', ' + str(node.endIndex) + ') level:' + str(node.level) + ' \"' + self.baseString[node.startIndex:node.endIndex] + '\"');
        else:
            return '';
    
    def PreOrderTraversal(self):
        self._preOrderTraversal(self.rootNode);
    
    def _preOrderTraversal(self, node):
        print(self._nodeFString(node));
        for child in node.children:
            self._preOrderTraversal(child);
    
    def MaxOverlap(self, inputStr):
        if(not inputStr): return 0;
        
        return self._maxOverlap(self.rootNode, inputStr + self.specialChar, 0);
    
    def _maxOverlap(self, node, inputStr, overlapLength):
        for child in node.children:
            nodeStr = self._nodeString(child);
            if(nodeStr.endswith(self.specialChar)):
#                print(nodeStr);
                nodeStr = nodeStr.rstrip(self.specialChar);
                if(inputStr.startswith(nodeStr)):
                    return (overlapLength + len(nodeStr));
            elif(inputStr.startswith(nodeStr)):
#                print(nodeStr, str(len(nodeStr)));
                return (self._maxOverlap(child, inputStr[len(nodeStr):], overlapLength + len(nodeStr)));
        
        return 0;

#class Main():
#    tree = SuffixTree('hello');
#    tree.PreOrderTraversal();
#    print('\n');
#    tree.PrintSuffixes();
#    print('\n');
#    print('Maximum Overlap length = ', tree.MaxOverlap('la'));
#    

    
    
