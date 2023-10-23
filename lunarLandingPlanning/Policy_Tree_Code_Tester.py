import gym
import joblib
from stable_baselines3 import PPO
import numpy as np
from tensorflow import keras as K
import statistics
import random
import copy as copy

whichEnv = 5
episodeMax = 10
seedList = random.sample(range(100, 1000), episodeMax)
printingCSV = True
#seed of importance: 0, 1, 10, 100
# seedList = [768]
# episodeMax = len(seedList)
theSeed = 0
agentList = [
    #["random",[]], 
    ["policy",[]], 
    ["tree",[]], 
    #["code",[]]
    ]
treeName = ""
csvFileName = ""
codePredict = []

if(whichEnv == 1):
    env = gym.make("LunarLander-v2")
    model = PPO.load("policies/ppo_lunar_policy_25e4T_04", env=env)
    classification_tree = joblib.load("decisionTrees/ppo_lunar_policy_25e4T_04_decision_tree_02")
    csvFileName = "CSV_ppo_lunar_policy_25e4T_04_10eps_results_forFunsies"
    from generatedCode.betterlanderCode import predict as LunarLanderPredict01
    codePredict = LunarLanderPredict01
    usesKeras = False
elif(whichEnv == 2):
    env = gym.make("LunarLander-v2")
    model = PPO.load("policies/ppo_lunar_policy_25e4T_04", env=env)
    classification_tree = joblib.load("decisionTrees/ppo_lunar_policy_25e4T_04_decision_tree_40eps")
    csvFileName = "CSV_ppo_lunar_policy_25e4T_04_40eps_results"
    from generatedCode.Tree40epLanderCodeNoRounding import predict as LunarLanderPredict02
    codePredict = LunarLanderPredict02
    usesKeras = False
elif(whichEnv == 3):
    env = gym.make("CartPole-v1")
    model = PPO.load("policies/ppo_cartPole_policy_25e4T_01", env=env)
    classification_tree = joblib.load("decisionTrees/ppo_cartPole_policy_25e4T_01_decision_tree_alpha_013x10e-3")
    csvFileName = "CSV_ppo_cartPole_policy_25e4T_01_10eps_results_02"
    from generatedCode.Tree10epCartPoleCode import predict as CartPoleCode
    codePredict = CartPoleCode
    usesKeras = False
elif(whichEnv == 4):
    env = gym.make("LunarLander-v2")
    model = PPO.load("policies/ppo_lunar_policy_25e4T_04", env=env)
    treeName = "decisionTrees/ppo_lunar_policy_25e4T_04_decision_tree_"
    classification_tree = joblib.load(treeName + "10eps")
    csvFileName = "CSV_ppo_lunar_policy_25e4T_04_10eps_results_forFunsies05"
    from generatedCode.Tree10epLanderCodeNoRounding import predict as LunarLanderPredict03
    codePredict = LunarLanderPredict03
    usesKeras = False
    agentList.append(["tree 40 eps",[]])
    agentList.append(["tree 100 eps",[]])
    agentList.append(["tree 200 eps",[]])
elif(whichEnv == 5):
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
elif(whichEnv == 6):
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
    
def printHorizontalCSV():
    headers = "Agents, Seed " + ", Seed ".join(str(x) for x in seedList) + ", Average Reward" +"\n"
    rows = ""
    for agent in agentList:
        rows += "\""+ agent[0] +"\", "+ ", ".join(str(x) for x in agent[1])+ "\n"
    csvString = headers + rows
    return csvString

def printVerticalCSV():
    headers = "Seeds"
    for agent in agentList:
        headers += ", "
        headers += agent[0]
    headers += "\n"
    rows = ""
    for i in range(episodeMax):
        rows += str(seedList[i])
        for agent in agentList:
            rows +=", "
            rows += str(agent[1][i]) 
        rows += "\n"
    csvString = headers + rows
    print(csvString)
    return csvString
    

for agent in agentList:
    if(agent[0] == "tree 40 eps"):
        classification_tree = classification_tree = joblib.load(treeName + "40eps")
    elif(agent[0] == "tree 100 eps"):
        classification_tree = classification_tree = joblib.load(treeName + "100eps")
    elif(agent[0] == "tree 200 eps"):
        classification_tree = classification_tree = joblib.load(treeName + "200eps")
    runAgent(agent, usesKeras)

#printVerticalCSV()
if(printingCSV):
    f = open("assets/"+csvFileName +".csv", "w")
    f.write(printVerticalCSV())

env.close()
