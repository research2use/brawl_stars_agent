import cv2
import gym
import numpy as np
from brawl_stars_gym.try_brawler import TryBrawler


class RandomAgent(object):
    """The world's simplest agent!"""

    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation, reward, done):
        return self.action_space.sample()


env = gym.make(
    "BrawlStarsTryBrawler-v0",
    ldplayer_executable_filepath=r"D:\\LDPlayer\\LDPlayer4.0\\dnplayer.exe",
    # fps=10,
)

agent = RandomAgent(env.action_space)
episode_count = 100
reward = 0
done = False

for i in range(episode_count):
    ob = env.reset()
    while True:
        action = agent.act(ob, reward, done)
        ob, reward, done, _ = env.step(action)
        if done:
            break
        # Note there's no env.render() here. But the environment still can open window and
        # render if asked by env.monitor: it calls env.render('rgb_array') to record video.
        # Video is not recorded every episode, see capped_cubic_video_schedule for details.
        # env.render()
# Close the env and write monitor result info to disk
env.close()
