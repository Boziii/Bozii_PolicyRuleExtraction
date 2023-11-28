import gym
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot as plt
import joblib


env = gym.make("LunarLander-v2")


stateDataset = joblib.load("assets/ppo_lunar_200eps_states")
actionDataset = joblib.load("assets/ppo_lunar_200eps_actions")

doGraphs = False
if(doGraphs):
    clf = DecisionTreeClassifier(random_state=0)
    path = clf.cost_complexity_pruning_path(stateDataset, actionDataset)
    ccp_alphas, impurities = path.ccp_alphas, path.impurities
    
    fig, ax = plt.subplots()
    ax.plot(ccp_alphas[:-1], impurities[:-1], marker="o", drawstyle="steps-post")
    ax.set_xlabel("effective alpha")
    ax.set_ylabel("total impurity of leaves")
    ax.set_title("Total Impurity vs effective alpha for training set")
    fig.savefig("assets/graph_impurity_VS_alpha.png")
    plt.show()
    
    clfs = []
    print("The number of alphas: ", len(ccp_alphas))
    
    alphaCounter = 0
    trimmedAlphaList = ccp_alphas[-100:]
    for ccp_alpha in ccp_alphas[-100:]:
        print(alphaCounter, "\t\t Alpha--> ", ccp_alpha)
        clf = DecisionTreeClassifier(random_state=0, ccp_alpha=ccp_alpha)
        clf.fit(stateDataset, actionDataset)
        clfs.append(clf)
        alphaCounter += 1
    print(
        "Number of nodes in the last tree is: {} with ccp_alpha: {}".format(
            clfs[-1].tree_.node_count, ccp_alphas[-1]
        )
    )
    
    clfs = clfs[:-1]
    ccp_alphas = trimmedAlphaList[:-1]
    
    node_counts = [clf.tree_.node_count for clf in clfs]
    depth = [clf.tree_.max_depth for clf in clfs]
    fig, ax = plt.subplots(2, 1)
    ax[0].plot(ccp_alphas, node_counts, marker="o", drawstyle="steps-post")
    ax[0].set_xlabel("alpha")
    ax[0].set_ylabel("number of nodes")
    ax[0].set_title("Number of nodes vs alpha")
    ax[1].plot(ccp_alphas, depth, marker="o", drawstyle="steps-post")
    ax[1].set_xlabel("alpha")
    ax[1].set_ylabel("depth of tree")
    ax[1].set_title("Depth vs alpha")
    fig.tight_layout()
    fig.savefig("assets/graph_node_number_and_deph_VS_alpha.png")
    plt.show()
    
    test_scores = [clf.score(stateDataset, actionDataset) for clf in clfs]
    
    fig, ax = plt.subplots()
    ax.set_xlabel("alpha")
    ax.set_ylabel("accuracy")
    ax.set_title("Accuracy vs alpha for training and testing sets")
    ax.plot(ccp_alphas, test_scores, marker="o", label="test", drawstyle="steps-post")
    ax.legend()
    fig.savefig("assets/accuracy_VS_alpha.png")
    plt.show()
else:
    landerFeatureNames = ["lander x", "lander y", "x velocity", "y velocity", "angle", "angle velocity", "left leg contact", "right leg contact"]
    landerTargetNames = ["nothing", "left engine", "main engine", "right engine"]
    classification_tree = tree.DecisionTreeClassifier()#random_state=0, ccp_alpha=0.0001)
    
    stateDataset10eps = stateDataset[0:10]
    stateDataset40eps = stateDataset[0:40]
    stateDataset100eps = stateDataset[0:100]
    
    actionDataset10eps = actionDataset[0:10]
    actionDataset40eps = actionDataset[0:40]
    actionDataset100eps = actionDataset[0:100]
    print(len(actionDataset))
    
    classification_tree = classification_tree.fit(stateDataset100eps, actionDataset100eps)
    #text_representation = tree.export_text(classification_tree)
    print("depth: ", classification_tree.tree_.max_depth)
    print("node count: ", classification_tree.tree_.node_count)
    print("accuracy: ", classification_tree.score(stateDataset, actionDataset))
    
    currentRewardForEpisode= 0
    stepcount = 0
    episodeCount = 1
    done = False
    
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
    
    
    fig = plt.figure(figsize=(15,15))
    _ = tree.plot_tree(classification_tree, 
                       feature_names=landerFeatureNames,  
                       class_names=landerTargetNames,
                       filled=True,
                       fontsize = 10)
    
    fig.savefig("assets/lander_200eps_decistion_tree_pruned.png")