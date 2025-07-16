import time
import torch
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from snake_env import Snake

def main():
    env = make_vec_env(lambda: Snake(width=20), n_envs=1)
    model = PPO('MlpPolicy', env, verbose=1, tensorboard_log="./snake_tensorboard")
    print("Training...")
    start_time = time.time()
    model.learn(total_timesteps=40000)
    end_time = time.time()
    print(f"Training took {round(end_time - start_time, 2)} seconds.")
    model.save("./snake_model_sb3")

if __name__ == "__main__":
    main() 