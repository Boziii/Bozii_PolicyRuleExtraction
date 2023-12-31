import gym


from sklearn import tree
from matplotlib import pyplot as plt
import joblib
from ruleExtractor import ruleExtractor
from featureClass import envFeature
from featureClass import getCartPoleFeaturesAndTarget
from featureClass import getLanderFeaturesAndTarget
from featureClass import getMountainCarFeaturesAndTarget
from codeGenerator import codeGenerator








#classification_tree = joblib.load("decisionTrees/ppo_cartPole_policy_25e4T_01_decision_10eps")
# classification_tree = joblib.load( "decisionTrees/BDT_20231102/ppo_cartPole_policy_25e4T_01_BDT_20231102_10eps")
# landerFeatures, landerTargetNames = getCartPoleFeaturesAndTarget()
# codeFileName = "Tree10epCartPoleCodeNoRounding"
# env = gym.make("CartPole-v1")

classification_tree = joblib.load("decisionTrees/BDT_20231102/dqn_MountainCar_policy_BDT_20231102_10eps")
landerFeatures, landerTargetNames = getMountainCarFeaturesAndTarget()
codeFileName = "Tree10epMountainCarCodeNoRounding"
env = gym.make("MountainCar-v0")

#classification_tree = joblib.load("decisionTrees/ppo_lunar_policy_25e4T_04_decision_tree_02")
#classification_tree = joblib.load("decisionTrees/ppo_lunar_policy_25e4T_04_decision_tree_alpha_013x10e-3")
#classification_tree = joblib.load("decisionTrees/ppo_lunar_policy_25e4T_04_decision_tree_10eps")
#classification_tree = joblib.load("decisionTrees/ppo_lunar_policy_25e4T_04_decision_tree_40eps")
#classification_tree = joblib.load("decisionTrees/ppo_lunar_policy_25e4T_04_decision_tree_10eps")
# classification_tree = joblib.load("decisionTrees/BDT_20231102/ppo_lunar_policy_25e4T_04_BDT_20231102_10eps")
# landerFeatures, landerTargetNames = getLanderFeaturesAndTarget()
# codeFileName = "Tree10epLanderCodeNoRounding"
# env = gym.make("LunarLander-v2")

text_representation = tree.export_text(classification_tree)
print(text_representation)

obs = env.reset()

ruleExtractorVar = ruleExtractor()



print(list(map(lambda feature: feature.name,landerFeatures)))


ruleExtractorVar.get_rules(classification_tree, landerFeatures, landerTargetNames)

for r in ruleExtractorVar.printedTreeRules:
    print(r)

ruleTrees = ruleExtractorVar.make_rule_trees(classification_tree, landerFeatures, landerTargetNames)

cgVar = codeGenerator(codeFileName, landerFeatures, landerTargetNames)
cgVar.ruleTrees = ruleTrees
cgVar.printToFile()
#  
currentRewardForEpisode= 0
stepcount = 0
episodeCount = 1
done = False
while episodeCount <= 10 or done==False:
    action= classification_tree.predict([obs])
    #print(action[0])
    obs, rewards, done, info = env.step(action[0])
    currentRewardForEpisode += rewards
    env.render()
    stepcount += 1
    if(done):
        print("step ", stepcount, "\t episode",episodeCount," - ",  currentRewardForEpisode)
        currentRewardForEpisode= 0
        episodeCount += 1
        obs = env.reset()
        


env.close()