import gym
import joblib
from stable_baselines3 import PPO
import numpy as np
from tensorflow import keras as K
import statistics
import random
import copy as copy
from matplotlib import pyplot as plt

whichEnv = 1
episodeMax = 1
seedList = random.sample(range(100, 1000), episodeMax)
#printingCSV = True
#seed of importance: 0, 1, 10, 100
# episodeMax = 3
seedList = [10]
theSeed = 0
agentList = [
    ["random",[]], 
    ["policy",[]], 
    #["tree",[]], 
    ["code",[]]
    ]
treeName = ""
csvFileName = ""
codePredict = []
rewardsPlot = []

if(whichEnv == 1):
    env = gym.make("LunarLander-v2")
    model = PPO.load("policies/ppo_lunar_policy_25e4T_04", env=env)
    treeName = "decisionTrees/ppo_lunar_policy_25e4T_04_decision_tree_"
    classification_tree = joblib.load(treeName + "10eps")
    csvFileName = "CSV_ppo_lunar_policy_25e4T_04_10eps_results_forFunsies03"
    from generatedCode.Tree10epLanderCodeNoRounding import predict as LunarLanderPredict03
    codePredict = LunarLanderPredict03
    usesKeras = False
    agentList.append(["tree 40 eps",[]])
    #agentList.append(["tree 100 eps",[]])
    agentList.append(["tree 200 eps",[]])
elif(whichEnv == 2):
    env = gym.make("CartPole-v1")
    model = PPO.load("policies/ppo_cartPole_policy_25e4T_01", env=env)
    treeName = "decisionTrees/ppo_cartPole_policy_25e4T_01_decision_"
    classification_tree = joblib.load(treeName + "10eps")
    csvFileName = "CSV_ppo_cartPole_policy_25e4T_01_10eps_results_forFunsies"
    from generatedCode.Tree10epCartPoleCodeNoRounding import predict as CartPoleCode01
    codePredict = CartPoleCode01
    usesKeras = False
    agentList.append(["tree 40 eps",[]])
    agentList.append(["tree 100 eps",[]])
    agentList.append(["tree 200 eps",[]])
elif(whichEnv == 3):
    env = gym.make("MountainCar-v0")
    model = K.models.load_model('{}'.format("policies/MountainCar-v0_target_model_1543419126.88.h5"))
    treeName = "decisionTrees/kera_MountainCar_policy_decision_tree_"
    classification_tree = joblib.load(treeName + "10eps")
    csvFileName = "CSV_kera_MountainCar_policy_10eps_results_forFunsies"
    from generatedCode.Tree10epMountainCarCode import predict as MountainCarCode
    codePredict = MountainCarCode
    usesKeras = True
    agentList.append(["tree 40 eps",[]])
    agentList.append(["tree 100 eps",[]])
    agentList.append(["tree 200 eps",[]])
else:
    env = gym.make("MountainCar-v0")
    model = K.models.load_model('{}'.format("policies/MountainCar-v0_target_model_1543419126.88.h5"))
    classification_tree = joblib.load("decisionTrees/kera_MountainCar_policy_decision_tree_10eps")
    csvFileName = "CSV_kera_MountainCar_policy_10eps_results"
    from generatedCode.Tree10epMountainCarCode import predict as MountainCarCode01
    codePredict = MountainCarCode01
    usesKeras = True

env.seed(theSeed)
obs = env.reset()


def runAgent(agent, useKeras):
    agentType = agent[0]
    currentRewardForEpisode= 0
    stepcount = 0
    done = False
    
    print("Now with the", agentType)
    episodeCount = 0
    env.seed(seedList[episodeCount])
    obs = env.reset()
    episodeRewards = []
    while episodeCount < episodeMax or done==False:
        if(agentType == "random"):
            action= env.action_space.sample()
        elif(agentType == "policy" and useKeras == False):
            action, _states = model.predict(obs, deterministic=True)
        elif(agentType == "policy" and useKeras == True):
            reshapedObs = np.reshape(obs, [-1, env.observation_space.shape[0]])
            action = np.argmax(model.predict(reshapedObs, verbose=0))
        elif(agentType == "tree" or agentType == "tree 40 eps" or agentType == "tree 100 eps" or agentType == "tree 200 eps"):
            action= classification_tree.predict([obs])
            action = action[0]
        elif(agentType == "code"):
            action= codePredict(obs)
        obs, rewards, done, _ = env.step(action)
        currentRewardForEpisode += rewards
        rewardsPlot.append(currentRewardForEpisode)
        env.render()
        stepcount += 1
        if(done):
            print("step ", stepcount, "\t seed", seedList[episodeCount], "\t episode",episodeCount," - ",  currentRewardForEpisode)
            episodeRewards.append(currentRewardForEpisode)
            currentRewardForEpisode= 0
            episodeCount += 1
            if(episodeCount < episodeMax):
                env.seed(seedList[episodeCount])
            obs = env.reset()
    averageEpisodeReward = statistics.mean(episodeRewards)
    agent[1] = copy.deepcopy(episodeRewards)
    agent[1].append(averageEpisodeReward)
    print("Average Reward: ", averageEpisodeReward, "\n")
        
fig, ax = plt.subplots()
ax.set_xlabel("time step")
ax.set_ylabel("cumulative reward")
ax.set_title("Cumulative Reward Over Time")
ax.axhline(y=0, color='r', linestyle='-')
for agent in agentList:
    if(agent[0] == "tree 40 eps"):
        classification_tree = classification_tree = joblib.load(treeName + "40eps")
    elif(agent[0] == "tree 100 eps"):
        classification_tree = classification_tree = joblib.load(treeName + "100eps")
    elif(agent[0] == "tree 200 eps"):
        classification_tree = classification_tree = joblib.load(treeName + "200eps")
    rewardsPlot=[]
    runAgent(agent, usesKeras)
    ax.plot(rewardsPlot, marker=".", label=agent[0], drawstyle="default")
ax.legend()
plt.show() 
fig.savefig("assets/graph_cumulative_reward_over_time.png")



env.close()