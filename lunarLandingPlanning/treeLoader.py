import gym


from sklearn import tree
from matplotlib import pyplot as plt
import joblib
from ruleExtractor import ruleExtractor
from featureClass import envFeature
from codeGenerator import codeGenerator

env = gym.make("LunarLander-v2")


classification_tree = joblib.load("decisionTrees/ppo_lunar_policy_25e4T_04_decision_tree_02")
#classification_tree = joblib.load("decisionTrees/ppo_lunar_policy_25e4T_04_decision_tree_alpha_013x10e-3")

text_representation = tree.export_text(classification_tree)
print(text_representation)

obs = env.reset()
#print(obs)
#test comment


ruleExtractorVar = ruleExtractor()
landerFeatureNames = ["lander_x", "lander_y", "x_velocity", "y_velocity", "angle", "angle_velocity", "left_leg_contact", "right_leg_contact"]
landerFeatureTypes = ["number", "number", "number", "number", "number", "number", "bool", "bool"]
landerFeatures = []
for i in range(0, 8):
    landerFeatures.append(envFeature(landerFeatureNames[i], landerFeatureTypes[i]))
    #print(landerFeatures.features[i].name)
    
print(list(map(lambda feature: feature.name,landerFeatures)))

landerTargetNames = ["nothing", "left_engine", "main_engine", "right_engine"]
ruleExtractorVar.get_rules(classification_tree, landerFeatures, landerTargetNames)

for r in ruleExtractorVar.printedTreeRules:
    print(r)

ruleTrees = ruleExtractorVar.make_rule_trees(classification_tree, landerFeatures, landerTargetNames)

cgVar = codeGenerator("betterlanderCode", landerFeatures, landerTargetNames)
cgVar.ruleTrees = ruleTrees
cgVar.printToFile()

currentRewardForEpisode= 0
stepcount = 0
episodeCount = 1
done = False
while stepcount <= 2000 or done==False:
    action= classification_tree.predict([obs])
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