import pygame
import random
import numpy as np
import gymnasium as gym
from gymnasium import spaces

class Snake(gym.Env):
    metadata = {'render_modes': ['human']}
    def __init__(self, width=20, render_mode=None):
        super().__init__()
        self.width = width
        self.height = width
        self.thickness = 10
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=1, shape=(12,), dtype=np.float32)
        self.render_mode = render_mode
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.white = (255, 255, 255)
        self.brown = (165, 42, 42)
        self.window = None
        self.clock = None
        self.reset()
    def reset(self, *, seed=None, options=None):
        super().reset(seed=seed)
        self.snakePos = [10, 5]
        self.snakeBody = [[10,5], [9,5], [8,5]]
        self.foodPos = [random.randint(1, self.width-2), random.randint(1, self.width-2)]
        self.direction = 'RIGHT'
        self.score = 0
        self.game_over = False
        obs = self.get_state()
        info = {}
        if self.render_mode == 'human':
            self._render_frame()
        return obs, info
    def step(self, action):
        direction = ['UP', 'DOWN', 'LEFT', 'RIGHT'][action]
        if direction == 'RIGHT' and not self.direction == 'LEFT':
            self.direction = 'RIGHT'
        elif direction == 'LEFT' and not self.direction == 'RIGHT':
            self.direction = 'LEFT'
        elif direction == 'UP' and not self.direction == 'DOWN':
            self.direction = 'UP'
        elif direction == 'DOWN' and not self.direction == 'UP':
            self.direction = 'DOWN'
        if self.direction == 'RIGHT': self.snakePos[0] += 1
        elif self.direction == 'LEFT': self.snakePos[0] -= 1
        elif self.direction == 'UP': self.snakePos[1] -= 1
        elif self.direction == 'DOWN': self.snakePos[1] += 1
        self.snakeBody.insert(0, list(self.snakePos))
        reward = 0
        if self.snakePos == self.foodPos:
            self.score += 1
            self.foodPos = [random.randint(1, self.width-2), random.randint(1, self.width-2)]
            reward = 10
        else:
            self.snakeBody.pop()
        self.check_game_over()
        terminated = self.game_over
        truncated = False
        obs = self.get_state()
        info = {}
        if self.render_mode == 'human':
            self._render_frame()
        return obs, reward, terminated, truncated, info
    def _render_frame(self):
        if self.window is None:
            pygame.init()
            self.window = pygame.display.set_mode((self.width*self.thickness, self.width*self.thickness))
            pygame.display.set_caption('Snake AI')
            self.clock = pygame.time.Clock()
        self.window.fill(self.white)
        # Draw snake body
        for i, pos in enumerate(self.snakeBody):
            if i == 0:
                # Draw head with a different color
                pygame.draw.rect(self.window, self.green,
                                 pygame.Rect(pos[0]*self.thickness, pos[1]*self.thickness, self.thickness, self.thickness))
                # Draw eyes
                cx = pos[0]*self.thickness
                cy = pos[1]*self.thickness
                eye_radius = self.thickness // 6
                offset = self.thickness // 4
                # Eyes position based on direction
                if self.direction == 'UP':
                    eye1 = (cx + offset, cy + offset)
                    eye2 = (cx + self.thickness - offset, cy + offset)
                elif self.direction == 'DOWN':
                    eye1 = (cx + offset, cy + self.thickness - offset)
                    eye2 = (cx + self.thickness - offset, cy + self.thickness - offset)
                elif self.direction == 'LEFT':
                    eye1 = (cx + offset, cy + offset)
                    eye2 = (cx + offset, cy + self.thickness - offset)
                else:  # RIGHT
                    eye1 = (cx + self.thickness - offset, cy + offset)
                    eye2 = (cx + self.thickness - offset, cy + self.thickness - offset)
                pygame.draw.circle(self.window, (0,0,0), eye1, eye_radius)
                pygame.draw.circle(self.window, (0,0,0), eye2, eye_radius)
            else:
                pygame.draw.rect(self.window, self.green,
                                 pygame.Rect(pos[0]*self.thickness, pos[1]*self.thickness, self.thickness, self.thickness))
        # Draw food
        pygame.draw.rect(self.window, self.red,
                         pygame.Rect(self.foodPos[0]*self.thickness, self.foodPos[1]*self.thickness, self.thickness, self.thickness))
        pygame.display.flip()
        self.clock.tick(10)
    def render(self):
        self._render_frame()
    def close(self):
        if self.window is not None:
            pygame.quit()
            self.window = None
    def check_game_over(self):
        if any([
            self.snakePos[0] < 0 or self.snakePos[0] >= self.width,
            self.snakePos[1] < 0 or self.snakePos[1] >= self.height
        ]):
            self.game_over = True
        for block in self.snakeBody[1:]:
            if self.snakePos == block:
                self.game_over = True
    def get_state(self):
        head_x, head_y = self.snakePos
        food_x, food_y = self.foodPos
        dir_up = 1.0 if self.direction == 'UP' else 0.0
        dir_down = 1.0 if self.direction == 'DOWN' else 0.0
        dir_left = 1.0 if self.direction == 'LEFT' else 0.0
        dir_right = 1.0 if self.direction == 'RIGHT' else 0.0
        danger_left = 1.0 if [head_x - 1, head_y] in self.snakeBody or head_x == 0 else 0.0
        danger_right = 1.0 if [head_x + 1, head_y] in self.snakeBody or head_x == self.width - 1 else 0.0
        danger_up = 1.0 if [head_x, head_y - 1] in self.snakeBody or head_y == 0 else 0.0
        danger_down = 1.0 if [head_x, head_y + 1] in self.snakeBody or head_y == self.height - 1 else 0.0
        food_left = 1.0 if food_x < head_x else 0.0
        food_right = 1.0 if food_x > head_x else 0.0
        food_up = 1.0 if food_y < head_y else 0.0
        food_down = 1.0 if food_y > head_y else 0.0
        return np.array([
            food_left, food_right, food_up, food_down,
            dir_left, dir_right, dir_up, dir_down,
            danger_left, danger_right, danger_up, danger_down
        ], dtype=np.float32) 