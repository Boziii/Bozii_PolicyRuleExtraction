import gymnasium as gym

from generatedCode.poorlanderCode import predict as poorPredict
from generatedCode.betterlanderCode import predict as betterPredict

env = gym.make("LunarLander-v2", render_mode="human")
obs, info = env.reset()

currentRewardForEpisode= 0
stepcount = 0
episodeCount = 1
done = False
#env.render()
while stepcount <= 400 or done==False:
    action= [env.action_space.sample()]
    obs, rewards, terminated, truncated, info = env.step(action[0])
    done = terminated or truncated
    currentRewardForEpisode += rewards
    
    stepcount += 1
    if(done):
        print("step ", stepcount, "\t episode",episodeCount," - ",  currentRewardForEpisode)
        currentRewardForEpisode= 0
        episodeCount += 1
        obs, info = env.reset()


print("Now with Better Predict")
episodeCount = 1
#env.render()
while episodeCount <= 10 or done==False:
    action= [betterPredict(obs)]
    obs, rewards, terminated, truncated, info = env.step(action[0])
    done = terminated or truncated
    currentRewardForEpisode += rewards

    stepcount += 1
    if(done):
        print("step ", stepcount, "\t episode",episodeCount," - ",  currentRewardForEpisode)
        currentRewardForEpisode= 0
        episodeCount += 1
        obs, info = env.reset()
        


env.close()