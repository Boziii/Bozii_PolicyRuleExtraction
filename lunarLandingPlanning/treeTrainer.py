import gym
from sklearn import tree
from matplotlib import pyplot as plt
import joblib

class treeTrainer:


    def __init__(self, ppo_model):
        self.model = ppo_model 
        
    def makeTree(self, treeFileName):
        env = gym.make("LunarLander-v2")
        vec_env = self.model.get_env()
        obs = vec_env.reset()
        print(obs)
        print(obs[0])
        stateDataset = []
        actionDataset = []
        for i in range(4000):
            action, _states = self.model.predict(obs, deterministic=True)
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
        classification_tree = tree.DecisionTreeClassifier()
        
        #train our decision tree (tree induction and pruning)
        classification_tree = classification_tree.fit(stateDataset, actionDataset)
        
        joblib.dump(classification_tree, treeFileName)