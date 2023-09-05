
from sklearn import tree
import joblib
import ruleExtractor

from featureClass import envFeature

class codeGenerator:
    def __init__(self, name, features, targets):
        self.filename = name
        self.folder = "generatedCode"
        self.features = features
        self.targets = targets
        self.ruleTrees = []
        
    def loadTree(self,filename):
        classification_tree = joblib.load(filename)
        ruleExtractorVar = ruleExtractor()
        self.ruleTrees = ruleExtractorVar.make_rule_trees(classification_tree, self.features, self.targets)
        return 0
    
    def printToFile(self):
        f = open(self.folder+"/"+self.filename +".py", "w")
        
        f.write(self.generatePredictFunc())
        f.write(self.newLine(""))
        
        i = 0
        for target in self.targets:
            f.write(self.generateWeShould(target, self.ruleTrees[i]))
            i += 1
            f.write(self.newLine(""))
            f.write(self.newLine(""))

        f.close()
        return 0
    
    def newLine(self,indent):
        return "\n"+indent
        
    def generateWeShould(self, target, ruleTree):
        indent = "\t"
        commaJoiner =", "
        
        funcParam = commaJoiner.join(map(lambda feature: feature.name,self.features))
        funcText = "def weShould_"+target +"(" + funcParam +"):"
        funcText += self.newLine("") + ruleTree.toPython(indent)
        funcText += self.newLine(indent) + "return False"
        return funcText
    
    def generatePredictFunc(self):
        funcText = "def predict(observation):"
        indent = "\t"
        
        funcText += self.newLine(indent) + "action = 0"
        
#         for target in self.targets:
#             funcText += self.newLine(indent) + target + "= False"
        
        i=0
        for feature in self.features:
            funcText += self.newLine(indent) + feature.name + "= observation["+ str(i) +"]"
            i+=1
        funcText += self.newLine("")
        
        i=0
        commaJoiner =", "
        for target in self.targets:
            funcArg = commaJoiner.join(map(lambda feature: feature.name,self.features))
            funcText += self.newLine(indent) + "if weShould_"+target +"(" + funcArg +"):"
            funcText += self.newLine(indent+indent) + "action = " + str(i)
            i+=1
        
        funcText += self.newLine("")
        funcText += self.newLine(indent) + "return action"
        
        return funcText