import gym

from generatedCode.poorlanderCode import predict as poorPredict
from generatedCode.betterlanderCode import predict as betterPredict

env = gym.make("LunarLander-v2")
obs = env.reset()

currentRewardForEpisode= 0
stepcount = 0
episodeCount = 1
done = False
while stepcount <= 400 or done==False:
    action= [poorPredict(obs)]
    obs, rewards, done, info = env.step(action[0])
    currentRewardForEpisode += rewards
    env.render()
    stepcount += 1
    if(done):
        print("step ", stepcount, "\t episode",episodeCount," - ",  currentRewardForEpisode)
        currentRewardForEpisode= 0
        episodeCount += 1
        obs = env.reset()

print("Now with Better Predict")
while stepcount <= 2000 or done==False:
    action= [betterPredict(obs)]
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