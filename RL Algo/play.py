import time
from stable_baselines3 import PPO
from snake_env import Snake

def main():
    env = Snake(width=20, render_mode='human')
    model = PPO.load("snake_model_sb3")
    obs, info = env.reset()
    done = False
    total_reward = 0
    while True:
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, terminated, truncated, info = env.step(action)
        env.render()
        total_reward += reward
        time.sleep(0.05)
        if terminated or truncated:
            print(f"Episode finished. Total reward: {total_reward}")
            obs, info = env.reset()
            total_reward = 0

if __name__ == "__main__":
    main() 