from sympy.physics.units.definitions.dimension_definitions import action
import numpy as np
from featureClass import envFeature

class conditionClass:
    def __init__(self, feature, threshold, isLeftChild):
        self.feature = feature
        self.isLeftChild = isLeftChild
        if feature.type == "number":
            self.threshold = threshold
            if isLeftChild:
                self.binaryOp = "<="
            else:
                self.binaryOp = ">"
        elif feature.type == "bool":
            self.threshold = "True"
            if isLeftChild:
                self.binaryOp = "!="
            else:
                self.binaryOp = "=="
        
    def negateOp(self):
        if self.binaryOp == "<=":
            self.binaryOp = ">"
        elif self.binaryOp == "!=":
            self.binaryOp = "=="
        elif self.binaryOp == ">":
            self.binaryOp = "<="
        elif self.binaryOp == "==":
            self.binaryOp = "!="
    
    def getConditionString(self):
        conditionString = ""
        if self.feature.type == "number":
            #conditionString = f"({self.feature.name} {self.binaryOp} {np.round(self.threshold, 3)})"
            conditionString = f"({self.feature.name} {self.binaryOp} {self.threshold})"
        elif self.feature.type == "bool":
            conditionString = f"({self.feature.name} {self.binaryOp} {self.threshold})"
        return conditionString
        
    def toString(self):
        conditionString = "if"+self.getConditionString()+" then"
        return conditionString
    
    def toPython(self):
        conditionString = "if"+self.getConditionString()+":"
        return conditionString

class actionLeaf:
    def __init__(self, classNames, action):
        self.chosenAction = action
        self.actionString = classNames[action]
        
    def toString(self):
        return self.actionString
    
    def toPython(self):
        return "return True"

        
class ruleTreeNode:
    def __init__(self, condition):
        self.nodeID = None
        self.rightChild = None
        self.leftChild = None
        self.data = condition
        
    def linkChain(self, nodeToAdd, whichWay):
        if(self.leftChild != None):
            self.leftChild.linkChain(nodeToAdd, whichWay)
        elif(self.rightChild != None):
            self.rightChild.linkChain(nodeToAdd, whichWay)
        elif(self.leftChild == None and self.rightChild == None):
            if(whichWay == "left"):
                self.leftChild = nodeToAdd
            elif(whichWay == "right"):
                self.rightChild = nodeToAdd
    
    def negateOpInLastLink(self):
        if(self.leftChild != None):
            self.leftChild.negateOpInLastLink()
        elif(self.rightChild != None):
            self.rightChild.negateOpInLastLink()
        elif(self.leftChild == None and self.rightChild == None):
            self.data.negateOp()
        
    def toString(self):
        treeString = ""
        if(self.data == []):
            treeString = "NEVER!"
        else:
            treeString += self.toStringHelper("")
        return treeString
    
    def toStringHelper(self, indent):
        treeString = ""
        oldIndent = indent
        indent += "|   "
        treeString = oldIndent + self.data.toString()
        if(self.leftChild != None):
            treeString += " L\n"+self.leftChild.toStringHelper(indent)
            if(self.rightChild != None):
                treeString += "\n"+oldIndent+"else"
                treeString += "\n"+self.rightChild.toStringHelper(indent)
        elif(self.rightChild != None):
            treeString += " R\n"+self.rightChild.toStringHelper(indent)
        return treeString
    
    def toPython(self, indent):
        treeString = ""
        if(self.data != []):
            treeString += self.toPythonHelper(indent)
        return treeString
    
    def toPythonHelper(self, indent):
        treeString = ""
        oldIndent = indent
        indent += "\t"
        treeString = oldIndent + self.data.toPython()
        if(self.leftChild != None):
            treeString += "\n"+self.leftChild.toPythonHelper(indent)
            if(self.rightChild != None):
                treeString += "\n"+oldIndent+"else:"
                treeString += "\n"+self.rightChild.toPythonHelper(indent)
        elif(self.rightChild != None):
            treeString += "\n"+self.rightChild.toPythonHelper(indent)
        return treeString
            
class sNode:
    def __init__(self, tree1, tree2):
        self.tree1 = tree1
        self.tree2 = tree2
#             