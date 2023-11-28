import gym
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot as plt
import joblib

from featureClass import getCartPoleFeaturesAndTarget
from featureClass import getLanderFeaturesAndTarget
from featureClass import getMountainCarFeaturesAndTarget

agentList = []
treeName = ""
csvFileName = ""
envList = []

treeName = "decisionTrees/BDT_20231102/ppo_cartPole_policy_25e4T_01_BDT_20231102_"
envList.append(["CartPole", treeName])

treeName = "decisionTrees/BDT_20231102/dqn_MountainCar_policy_BDT_20231102_"
envList.append(["MountainCar", treeName])

treeName = "decisionTrees/BDT_20231102/ppo_lunar_policy_25e4T_04_BDT_20231102_"
envList.append(["LunarLander", treeName])



treeEpisodeCountList = ["10eps", "40eps", "100eps", "200eps"] 
rowList = []
depthCountList = []
headers = "# of training episodes, max depth, node count, max depth, node count, max depth, node count"
rows = ""

for epCount in treeEpisodeCountList:
    for env in envList:
        classification_tree = joblib.load(env[1] + epCount)
        print(env[0])
        print("max depth: ", classification_tree.tree_.max_depth)
        print("node count: ", classification_tree.tree_.node_count)
        print("------")
        
        landerFeatures, landerTargetNames = [],[]
        fig = []
        if(env[0] == "CartPole"):
            landerFeatures, landerTargetNames = getCartPoleFeaturesAndTarget()
            fig = plt.figure(figsize=(20,6))
        elif(env[0] == "MountainCar"):
            landerFeatures, landerTargetNames = getMountainCarFeaturesAndTarget()
            fig = plt.figure(figsize=(9,6))
        elif(env[0] == "LunarLander"):
            landerFeatures, landerTargetNames = getLanderFeaturesAndTarget()
            fig = plt.figure(figsize=(50,6))
        landerFeatureNames = list(map(lambda feature: feature.name,landerFeatures))
        _ = tree.plot_tree(classification_tree, 
                           #feature_names=landerFeatureNames,  
                           class_names=landerTargetNames,
                           #label = 'none',
                           rounded = True,
                           filled=True,
                           fontsize = 4)
        treePicFileName = "assets/tree_pics/"+env[0]+"_tree"+epCount+".png"
        fig.savefig(treePicFileName)
        plt.close(fig)
        
        rowList.append(str(classification_tree.tree_.max_depth))
        rowList.append(str(classification_tree.tree_.node_count))
    rows += epCount +", " + ", ".join(rowList) +"\n"
    rowList = []
    print("=======================================")
    
print(headers)
print(rows)


f = open("assets/"+"treeDepthNodeCount" +".csv", "w")
f.write(headers+"\n")
f.write(rows)