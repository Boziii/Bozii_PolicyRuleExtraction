import gym
import joblib
from stable_baselines3 import PPO
from sklearn import tree
import statistics



# env = gym.make("LunarLander-v2")
# model = PPO.load("policies/ppo_lunar_policy_25e4T_04", env=env)
# classification_tree = joblib.load("decisionTrees/ppo_lunar_policy_25e4T_04_decision_tree_02")
# from generatedCode.betterlanderCode import predict as codePredict

env = gym.make("CartPole-v1")
model = PPO.load("policies/ppo_cartPole_policy_25e4T_01", env=env)
classification_tree = joblib.load("decisionTrees/ppo_cartPole_policy_25e4T_01_decision_tree_alpha_013x10e-3")
from generatedCode.betterCartPoleCode import predict as codePredict

obs = env.reset()


currentRewardForEpisode= 0
stepcount = 0
episodeCount = 1
done = False
print("Now with the Policy")
episodeCount = 1
vec_env = model.get_env()
obs = vec_env.reset()
episodeRewards = []
averageEpisodeReward = 0
while episodeCount <= 10 or done==False:
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, done, info = vec_env.step(action)
    currentRewardForEpisode += rewards
    vec_env.render()
    stepcount += 1
    if(done):
        print("step ", stepcount, "\t episode",episodeCount," - ",  currentRewardForEpisode[0])
        episodeRewards.append(currentRewardForEpisode[0])
        currentRewardForEpisode= 0
        episodeCount += 1
        obs = vec_env.reset()
averageEpisodeReward = statistics.mean(episodeRewards)
print("Average Reward: ", averageEpisodeReward, "\n")

print("Now with the Tree")
episodeCount = 1
obs = env.reset()
episodeRewards = []
averageEpisodeReward = 0
while episodeCount <= 10 or done==False:
    action= classification_tree.predict([obs])
    obs, rewards, done, info = env.step(action[0])
    currentRewardForEpisode += rewards
    env.render()
    stepcount += 1
    if(done):
        print("step ", stepcount, "\t episode",episodeCount," - ",  currentRewardForEpisode)
        episodeRewards.append(currentRewardForEpisode)
        currentRewardForEpisode= 0
        episodeCount += 1
        obs = env.reset()
averageEpisodeReward = statistics.mean(episodeRewards)
print("Average Reward: ", averageEpisodeReward, "\n")        

print("Now with the Code")
episodeCount = 1
obs = env.reset()
episodeRewards = []
averageEpisodeReward = 0
while episodeCount <= 10 or done==False:
    action= [codePredict(obs)]
    obs, rewards, done, info = env.step(action[0])
    currentRewardForEpisode += rewards
    env.render()
    stepcount += 1
    if(done):
        print("step ", stepcount, "\t episode",episodeCount," - ",  currentRewardForEpisode)
        episodeRewards.append(currentRewardForEpisode)
        currentRewardForEpisode= 0
        episodeCount += 1
        obs = env.reset()
averageEpisodeReward = statistics.mean(episodeRewards)
print("Average Reward: ", averageEpisodeReward, "\n") 

env.close()