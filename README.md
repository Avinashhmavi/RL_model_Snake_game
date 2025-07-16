# RL_model_Snake_game

A minimal, modern, reinforcement learning Snake game environment using Gymnasium and Stable Baselines3 (PyTorch). Includes training, evaluation, and GUI visualization.

## Features
- Custom Snake environment compatible with Gymnasium and SB3
- PPO agent training with Stable Baselines3
- Model saving/loading
- GUI visualization of the agent playing (with snake head and eyes)
- TensorBoard logging for training curves

## Setup

```bash
# Clone the repo
https://github.com/Avinashhmavi/RL_model_Snake_game.git
cd RL_model_Snake_game

# (Recommended) Create a Python 3.8+ virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Training

```bash
python train.py
```

## Evaluation

```bash
python evaluate.py
```

## Visualize Agent Playing (GUI)

```bash
python play.py
```

## Plot Training Curves

```bash
tensorboard --logdir=snake_tensorboard
# Open the provided URL in your browser
```

## Save/Load Models

- Models are saved as `snake_model_sb3.zip` after training.
- Load with: `model = PPO.load("snake_model_sb3")`

## Requirements
- Python 3.8+
- See `requirements.txt` for all dependencies

## Repo Structure
- `snake_env.py` - Custom Snake environment
- `train.py` - Training script
- `evaluate.py` - Evaluation script
- `play.py` - GUI visualization
- `requirements.txt` - Dependencies
- `README.md` - This file

---

**Author:** Avinashhmavi 