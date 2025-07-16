# Placeholder for TensorFlow.js export functionality
# This script is not required for SB3/PyTorch models, but can be adapted for ONNX or TorchScript export if needed.

# Example: Export to TorchScript
# from stable_baselines3 import PPO
# import torch
# from snake_env import Snake
#
# model = PPO.load("snake_model_sb3")
# traced = torch.jit.trace(model.policy, torch.zeros(1, 12))
# traced.save("snake_model_sb3.pt")

print("Export to TensorFlow.js is not directly supported for SB3/PyTorch models. Use ONNX or TorchScript if needed.") 