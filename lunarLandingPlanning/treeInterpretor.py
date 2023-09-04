from sklearn import tree
import joblib

class treeInterpretor:
    def __init__(self, decisionTree):
        self.decisionTree = decisionTree

    def interpret(self):
        count = 0
        self.decisionTree
        

c_tree = joblib.load("ppo_lunar_policy_25e4T_04_decision_tree_02")
#c_tree = joblib.load("ppo_lunar_policy_25e4T_04_decision_tree_alpha_013x10e-3")
text_representation = tree.export_text(c_tree)
print(text_representation)

landerFeatureNames = ["lander x", "lander y", "x velocity", "y velocity", "angle", "angle velocity", "left leg contact", "right leg contact"]
landerTargetNames = ["nothing", "left engine", "main engine", "right engine"]


theTree = c_tree.tree_
#list of doNothing
doNothingLeafs = []
#list of leftEngine
leftEngineLeafs = []
#list of mainEngine
mainEngineLeafs = []
#list of rightEngine
rightEngineLeafs = []

for i in range(theTree.node_count):
    if theTree.children_left[i] ==-1:
        leafDecidedClass = theTree.value[i][0]
        #print(i,", ",leafDecidedClass)
        if(leafDecidedClass[0] > 0):
            doNothingLeafs.append(i)
        if(leafDecidedClass[1] > 0):
            leftEngineLeafs.append(i)
        if(leafDecidedClass[2] > 0):
            mainEngineLeafs.append(i)
        if(leafDecidedClass[3] > 0):
            rightEngineLeafs.append(i)
    
print(doNothingLeafs)
print(leftEngineLeafs)
print(mainEngineLeafs)
print(rightEngineLeafs)