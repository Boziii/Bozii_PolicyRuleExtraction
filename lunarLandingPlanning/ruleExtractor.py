from sklearn.tree import _tree
import numpy as np
import copy as copy
from ruleClass import ruleTreeNode, sNode
from ruleClass import conditionClass
from ruleClass import actionLeaf
from featureClass import envFeature


class ruleExtractor:
    def __init__(self):
        self.printedTreeRules = []
        #self.codableTreeRules = []

    def get_rules(self, tree, featureList, class_names):
        tree_ = tree.tree_
        
        paths = []
        
        def recurse(node, path, paths):
            #if the feature value of a node is undefined, that indicates a node is a leaf node and thus a class
            if tree_.feature[node] != _tree.TREE_UNDEFINED:
                featVal = tree_.feature[node]
                threshold = tree_.threshold[node]
                
                p1, p2 = list(path), list(path)
                leftCondition = conditionClass(featureList[featVal], threshold, True)
                p1 += [leftCondition.getConditionString()]
                recurse(tree_.children_left[node], p1, paths)
                
                rightCondition = conditionClass(featureList[featVal], threshold, False)
                p2 += [rightCondition.getConditionString()]
                recurse(tree_.children_right[node], p2, paths)
            else:
                path += [(tree_.value[node], tree_.n_node_samples[node])]
                paths += [path]
                
        recurse(0, [], paths)
    
        # sort by samples count
        samples_count = [p[-1][1] for p in paths]
        ii = list(np.argsort(samples_count))
        paths = [paths[i] for i in reversed(ii)]
        
        rules = []
        for path in paths:
            rule = "if "
            
            for p in path[:-1]:
                if rule != "if ":
                    rule += " and "
                rule += str(p)
            rule += " then "
            if class_names is None:
                rule += "response: "+str(np.round(path[-1][0][0][0],3))
            else:
                classes = path[-1][0][0]
                l = np.argmax(classes)
                rule += f"class: {class_names[l]} (proba: {np.round(100.0*classes[l]/np.sum(classes),2)}%)"
            rule += f" | based on {path[-1][1]:,} samples"
            rules += [rule]
        
        self.printedTreeRules = rules
         
        return rules
    
            
    def make_rule_trees(self, tree, featureList, class_names):
        tree_ = tree.tree_
    
        ruleTreeBranchList = []
        
        def recurse(nodeIndex, nodeList, ruleTreeBranchList):
            
            if tree_.feature[nodeIndex] == _tree.TREE_UNDEFINED:
                #hit end of branch
                newTreeNode = ruleTreeNode( actionLeaf(class_names, np.argmax(tree_.value[nodeIndex])))
                if(nodeIndex in tree_.children_left):
                    nodeList[0].linkChain(newTreeNode, "left")
                else:
                    nodeList[0].linkChain(newTreeNode, "right")
                ruleTreeBranchList += [[np.argmax(tree_.value[nodeIndex]), nodeList]]
            else:
                
                n1, n2 = list(nodeList), list(copy.deepcopy(nodeList))
                
                featVal = tree_.feature[nodeIndex]
                threshold = tree_.threshold[nodeIndex]
                
                newTreeNode = ruleTreeNode(conditionClass(featureList[featVal], threshold, True))
                if(n1 == []):
                    n1.append(newTreeNode)
                else:
                    if(nodeIndex in tree_.children_left):
                        n1[0].linkChain(newTreeNode, "left")
                    else:
                        n1[0].linkChain(newTreeNode, "right")
                    #n1[0].linkChain(newTreeNode, "left")
                recurse(tree_.children_left[nodeIndex], n1, ruleTreeBranchList)
                    
                newTreeNode = ruleTreeNode(conditionClass(featureList[featVal], threshold, False))
                if(n2 == []):
                    n2.append(newTreeNode)
                else:
                    if(nodeIndex in tree_.children_left):
                        n2[0].linkChain(newTreeNode, "left")
                    else:
                        n2[0].linkChain(newTreeNode, "right")
                    #n2[0].linkChain(newTreeNode, "right")
                recurse(tree_.children_right[nodeIndex], n2, ruleTreeBranchList)
        

        recurse(0, [], ruleTreeBranchList)
        
        
        print("")
        for branch in ruleTreeBranchList:
            print("---")
            print(branch[1][0].toString())
            print("\n"+class_names[branch[0]])
            
        
              
#         
        ruleTreeList = []
        targetRules = []
        
        def mergeRuleTrees(ruletree1, ruletree2):
            if(not ruletree1):
                return ruletree2
            if(not ruletree2):
                return ruletree1
            
            s = []
            
            temp = sNode(ruletree1, ruletree2)
            s.append(temp)
            n = None
            
            while(len(s) != 0):
                n = s[-1]
                s.pop();
                
                if(n.left == None or n.right == None):
                    continue
                
                #n.left.data = n.right.data
                if(n.left.leftChild == None):
                    n.left.leftChild = n.right.leftChild
                else:
                    t=sNode(n.left.leftChild, n.right.leftChild)
                    s.append(t)
                
                if(n.left.rightChild == None):
                    n.left.rightChild = n.right.rightChild
                else:
                    t=sNode(n.left.rightChild, n.right.rightChild)
                    s.append(t)
            
            return ruletree1
#         
        def combineBranches(target, targetRules):
            ruleTreeVar = []
            for x in range(1,len(targetRules)):
                targetRules[0] = mergeRuleTrees(targetRules[0], targetRules[x])
            if(targetRules != []):
                ruleTreeVar = targetRules[0]
            else:
                ruleTreeVar = ruleTreeNode([])
            return ruleTreeVar         

        for target in class_names:
            for ruleBranch in ruleTreeBranchList:
                if class_names[ruleBranch[0]] == target:
                    targetRules.append(ruleBranch[1][0])
            ruleTreeList.append(combineBranches(target, targetRules))
            targetRules = []
        
        print("\n\n\n")
        print("# of rules: ", len(ruleTreeList))
        print("\n\n")
        for i in range(len(ruleTreeList)):
            print("When to do action: ", class_names[i])
            print(ruleTreeList[i].toString())
            print("\n\n")
    
        print("\n\n")
        
        return ruleTreeList
        
