
from stable_baselines3 import PPO
from sumo_env import SumoEnv
import time



model = PPO.load("PPO_MODEL")

env = SumoEnv(config_file="intersection.sumocfg", max_steps=500, use_gui=True)

obs = env.reset()

for _ in range(500):
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    time.sleep(0.1)

    if done:
        obs = env.reset()


env.close()


