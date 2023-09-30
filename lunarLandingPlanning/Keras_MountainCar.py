import gym
import numpy as np
from tensorflow import keras as K

from sklearn import tree
from matplotlib import pyplot as plt
from featureClass import getMountainCarFeaturesAndTarget
import joblib


envName = "MountainCar-v0"
env = gym.make(envName)

modelFileName = "policies/MountainCar-v0_target_model_1543419126.88.h5"
totalIters = 100
expectedReward = -110



model = K.models.load_model('{}'.format(modelFileName))
print("Saved model loaded from '{}'".format(model))
print("Starting testing.. Expecting reward to be {} over {} iterations".format(
    expectedReward, totalIters))

obs = env.reset()
print(obs)
print(obs[0])
print(env.action_space)

episodeCount = 1
stepcount = 0
currentRewardForEpisode = 0
done = False

stateDataset = []
actionDataset = []
for i in range(env.action_space.n):
    stateDataset.append(obs)
    actionDataset.append(i)
    
while episodeCount <= 10 or done==False:
    reshapedObs = np.reshape(obs, [-1, env.observation_space.shape[0]])
    action = np.argmax(model.predict(reshapedObs, verbose=0))
    stateDataset.append(obs)
    actionDataset.append(action)
    obs, rewards, done, info = env.step(action)
    currentRewardForEpisode += rewards
    env.render()
    stepcount += 1
    if(done):
        print("step ", stepcount, "\t episode",episodeCount," - ",  currentRewardForEpisode)
        currentRewardForEpisode= 0
        episodeCount += 1
        obs = env.reset()
        
env.close()


MountainCarFeatures, MountainCarTargetNames = getMountainCarFeaturesAndTarget()
#initialize our decision tree object
#classification_tree = tree.DecisionTreeClassifier(random_state=0, ccp_alpha=0.013)
classification_tree = tree.DecisionTreeClassifier()

#train our decision tree (tree induction and pruning)
classification_tree = classification_tree.fit(stateDataset, actionDataset)

joblib.dump(classification_tree, "decisionTrees/kera_MountainCar_policy_decision_tree_10eps")
del classification_tree
classification_tree = joblib.load("decisionTrees/kera_MountainCar_policy_decision_tree_10eps")


print("Now with the Tree")
episodeCount = 1
stepcount = 0
obs = env.reset()
while episodeCount <= 10 or done==False:
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


fig = plt.figure(figsize=(20,20))
_ = tree.plot_tree(classification_tree, 
                   feature_names=list(map(lambda feature: feature.name,MountainCarFeatures)),  
                   class_names=MountainCarTargetNames,
                   filled=True,
                   fontsize = 10)

fig.savefig("assets/mountain_decistion_tree01.png")