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
model = PPO.load("ppo_lunar_policy_25e4T_04", env=env)


# Evaluate the agent
# NOTE: If you use wrappers with your environment that modify rewards,
#       this will be reflected here. To evaluate with original rewards,
#       wrap environment in a "Monitor" wrapper before other wrappers.
mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)
print("mean reward: ", mean_reward)
print("std reward: ", std_reward)

# Enjoy trained agent
vec_env = model.get_env()
obs = vec_env.reset()
print(obs)
print(obs[0])
stateDataset = []
actionDataset = []
for i in range(4000):
    action, _states = model.predict(obs, deterministic=True)
    stateDataset.append(obs[0])
    actionDataset.append(action)
    obs, rewards, dones, info = vec_env.step(action)
    vec_env.render()


env.close()

landerFeatureNames = ["lander x", "lander y", "x velocity", "y velocity", "angle", "angle velocity", "left leg contact", "right leg contact"]
landerTargetNames = ["nothing", "left engine", "main engine", "right engine"]
print(landerFeatureNames)
print(landerTargetNames)

#initialize our decision tree object
classification_tree = tree.DecisionTreeClassifier(random_state=0, ccp_alpha=0.013)

#train our decision tree (tree induction and pruning)
classification_tree = classification_tree.fit(stateDataset, actionDataset)


#chang filename to right path
joblib.dump(classification_tree, "ppo_lunar_policy_25e4T_04_decision_tree_alpha_013x10e-3")
del classification_tree
classification_tree = joblib.load("ppo_lunar_policy_25e4T_04_decision_tree_alpha_013x10e-3")

text_representation = tree.export_text(classification_tree)
print(text_representation)

obs = vec_env.reset()
for i in range(1000):
    action= classification_tree.predict([obs[0]])
    obs, rewards, dones, info = vec_env.step(action)
    vec_env.render()


env.close()


fig = plt.figure(figsize=(300,50))
_ = tree.plot_tree(classification_tree, 
                   feature_names=landerFeatureNames,  
                   class_names=landerTargetNames,
                   filled=True,
                   fontsize = 10)

fig.savefig("assets/lander_decistion_tree01.png")




