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
episodeCount = 1
episodeMax = 200
done = False

vec_env = model.get_env()
obs = vec_env.reset()
print(obs)
print(obs[0])
stateDataset = []
actionDataset = []

while episodeCount <= episodeMax or done==False:
    action, _states = model.predict(obs, deterministic=True)
    stateDataset.append(obs[0])
    actionDataset.append(action)
    obs, rewards, done, info = vec_env.step(action)
    currentRewardForEpisode += rewards
    stepcount += 1
    vec_env.render()
    if(done):
        print("step ", stepcount, "\t episode",episodeCount," - ",  currentRewardForEpisode[0])
        currentRewardForEpisode= 0
        episodeCount += 1
        obs = vec_env.reset()
    

env.close()

landerFeatureNames = ["lander x", "lander y", "x velocity", "y velocity", "angle", "angle velocity", "left leg contact", "right leg contact"]
landerTargetNames = ["nothing", "left engine", "main engine", "right engine"]
print(landerFeatureNames)
print(landerTargetNames)

#initialize our decision tree object
#classification_tree = tree.DecisionTreeClassifier(random_state=0, ccp_alpha=0.013)
classification_tree = tree.DecisionTreeClassifier()

#train our decision tree (tree induction and pruning)
stateDataset10eps = stateDataset[:10]
stateDataset40eps = stateDataset[:40]
stateDataset100eps = stateDataset[:100]

actionDataset10eps = actionDataset[:10]
actionDataset40eps = actionDataset[:40]
actionDataset100eps = actionDataset[:100]

# classification_tree10eps = classification_tree.fit(stateDataset10eps, actionDataset10eps)
# classification_tree40eps = classification_tree.fit(stateDataset40eps, actionDataset40eps)
# classification_tree100eps = classification_tree.fit(stateDataset100eps, actionDataset100eps)
# classification_tree = classification_tree.fit(stateDataset, actionDataset)

joblib.dump(stateDataset, "assets/ppo_lunar_200eps_states")
joblib.dump(actionDataset, "assets/ppo_lunar_200eps_actions")


# joblib.dump(classification_tree10eps, "decisionTrees/ppo_lunar_pruned_tree_10eps")
# joblib.dump(classification_tree40eps, "decisionTrees/ppo_lunar_pruned_tree_40eps")
# joblib.dump(classification_tree100eps, "decisionTrees/ppo_lunar_pruned_tree_100eps")
# joblib.dump(classification_tree, "decisionTrees/ppo_lunar_pruned_tree_200eps")
# del classification_tree
# classification_tree = joblib.load("decisionTrees/ppo_lunar_pruned_tree_200eps")

#text_representation = tree.export_text(classification_tree)
#print(text_representation)

# print("Now with the Tree")
# episodeCount = 1
# stepcount = 0
# obs = env.reset()
# while episodeCount <= 10 or done==False:
#     action= classification_tree.predict([obs])
#     obs, rewards, done, info = env.step(action[0])
#     currentRewardForEpisode += rewards
#     env.render()
#     stepcount += 1
#     if(done):
#         print("step ", stepcount, "\t episode",episodeCount," - ",  currentRewardForEpisode)
#         currentRewardForEpisode= 0
#         episodeCount += 1
#         obs = env.reset()
# 
# env.close()
# 
# 
# fig = plt.figure(figsize=(50,50))
# _ = tree.plot_tree(classification_tree, 
#                    feature_names=landerFeatureNames,  
#                    class_names=landerTargetNames,
#                    filled=True,
#                    fontsize = 10)
# 
# fig.savefig("assets/lander_200eps_decistion_tree_pruned.png")
# 
# fig = plt.figure(figsize=(50,50))
# _ = tree.plot_tree(classification_tree10eps, 
#                    feature_names=landerFeatureNames,  
#                    class_names=landerTargetNames,
#                    filled=True,
#                    fontsize = 10)
# 
# fig.savefig("assets/lander_10eps_decistion_tree_pruned.png")
# 
# fig = plt.figure(figsize=(50,50))
# _ = tree.plot_tree(classification_tree100eps, 
#                    feature_names=landerFeatureNames,  
#                    class_names=landerTargetNames,
#                    filled=True,
#                    fontsize = 10)
# 
# fig.savefig("assets/lander_100eps_decistion_tree_pruned.png")




