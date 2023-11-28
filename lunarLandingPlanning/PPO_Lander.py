import gym

from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

#from StAcPair import StAcPair
from sklearn import tree
from matplotlib import pyplot as plt
import joblib

env = gym.make("LunarLander-v2")

#model = PPO("MlpPolicy", env, verbose=1)
# Train the agent and display a progress bar
#model.learn(total_timesteps=int(25e4), progress_bar=True)
# Save the agent
#model.save("ppo_lunar_policy_25e4T_05")
#del model  # delete trained model to demonstrate loading


# Load the trained agent
# NOTE: if you have loading issue, you can pass `print_system_info=True`
# to compare the system on which the model was trained vs the current one
# model = DQN.load("dqn_lunar", env=env, print_system_info=True)
model = PPO.load("policies/ppo_lunar_policy_25e4T_04", env=env)


# Evaluate the agent
# NOTE: If you use wrappers with your environment that modify rewards,
#       this will be reflected here. To evaluate with original rewards,
#       wrap environment in a "Monitor" wrapper before other wrappers.
mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)
print("mean reward: ", mean_reward)
print("std reward: ", std_reward)

# Enjoy trained agent
currentRewardForEpisode= 0
stepcount = 0
episodeCount = 0
episodeMax = 200
done = False

vec_env = model.get_env()
obs = vec_env.reset()
print(obs)
print(obs[0])
stateDataset = []
actionDataset = []
episodeStopPoint = []

while episodeCount < episodeMax or done==False:
    action, _states = model.predict(obs, deterministic=True)
    stateDataset.append(obs[0])
    actionDataset.append(action)
    obs, rewards, done, info = vec_env.step(action)
    currentRewardForEpisode += rewards
    stepcount += 1
    #vec_env.render()
    if(done):
        print("step ", stepcount, "\t episode",episodeCount," - ",  currentRewardForEpisode[0])
        currentRewardForEpisode= 0
        episodeCount += 1
        obs = vec_env.reset()
        if(episodeCount == 10 or episodeCount == 40 or episodeCount == 100 or episodeCount == 200):
            episodeStopPoint.append(len(actionDataset))
    

env.close()

landerFeatureNames = ["lander x", "lander y", "x velocity", "y velocity", "angle", "angle velocity", "left leg contact", "right leg contact"]
landerTargetNames = ["nothing", "left engine", "main engine", "right engine"]
print(landerFeatureNames)
print(landerTargetNames)

#initialize our decision tree object
#classification_tree = tree.DecisionTreeClassifier(random_state=0, ccp_alpha=0.013)
classification_tree = tree.DecisionTreeClassifier(random_state=0)

print("episode stop points:", episodeStopPoint)
treeName = "decisionTrees/BDT_20231102/ppo_lunar_policy_25e4T_04_BDT_20231102_"
assetFileLocation = "assets/stateAndActionCollections/ppo_lunar_"
xEpNamingList = ["10eps", "40eps", "100eps", "200eps"]
for i in range(4):
    xEpStateDataset = stateDataset[:episodeStopPoint[i]]
    xEpActionDataset = actionDataset[:episodeStopPoint[i]]
    classification_tree = classification_tree.fit(xEpStateDataset, xEpActionDataset)
    joblib.dump(classification_tree, treeName+xEpNamingList[i])
    joblib.dump(xEpStateDataset, assetFileLocation+xEpNamingList[i]+"_states")
    joblib.dump(xEpActionDataset, assetFileLocation+xEpNamingList[i]+"_actions")
    classification_tree = tree.DecisionTreeClassifier()
    
del classification_tree
classification_tree = joblib.load(treeName+"200eps")

#text_representation = tree.export_text(classification_tree)
#print(text_representation)

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





