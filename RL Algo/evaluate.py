import numpy as np
from stable_baselines3 import PPO
from snake_env import Snake

def evaluate(model, env, num_episodes=10):
    episode_rewards = []
    for ep in range(num_episodes):
        obs, info = env.reset()
        done = False
        total_reward = 0.0
        while not done:
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated
            total_reward += reward
        episode_rewards.append(total_reward)
        print(f"Episode {ep+1}: Reward = {total_reward}")
    mean_reward = np.mean(episode_rewards)
    print(f"Mean reward over {num_episodes} episodes: {mean_reward}")
    return mean_reward

def main():
    env = Snake(width=20)
    model = PPO.load("snake_model_sb3")
    evaluate(model, env)

if __name__ == "__main__":
    main() 