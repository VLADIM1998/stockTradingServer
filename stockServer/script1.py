import sys
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import pandas as pd
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3 import PPO
from stock.env.StockTradingEnv import StockTradingEnv
import time
import warnings
warnings.filterwarnings("ignore")



print('test')
# Read the data set
train = pd.read_csv('/Users/vladimerpurtskhvanidze/Desktop/MyWork/stockServer/stock/data/AAPL_train.csv')
# Sort the data by date
print('test1')
train = train.sort_values('Date')
print('test2')
print('test3')

# Train, Test Spilt
# train, test = train_test_split(df, test_size=0.2)
# The algorithms require a vectorized environment to run; Gym environment rendering
env = DummyVecEnv([lambda: StockTradingEnv(train)])
print('test3')
print('Training: Start...')


start_time = time.time()

# Model training
model = PPO('MlpPolicy', env, verbose=1)  # PPO
model.learn(total_timesteps=100)
end_time = time.time()
print('Training Time: ', end_time - start_time)
print('Training: Done!')

# Read the data set
test = pd.read_csv('/Users/vladimerpurtskhvanidze/Desktop/MyWork/stockServer/stock/data/AAPL_test.csv')
# Sort the data by date
test = train.sort_values('Date')
# Reset all the environments and return an array of observations, or a tuple of observation arrays.
test_env = DummyVecEnv([lambda: StockTradingEnv(test)])
obs = test_env.reset()

# Predict
for i in range(2000):
    action, _states = model.predict(obs)  # Get the policy action from an observation
    obs, rewards, done, info = env.step(action)
    env.render()

print('Training Time: ', end_time - start_time)

print('#Hello from python#')
# print('First param:'+sys.argv[1]+'#')
# print('Second param:'+sys.argv[2]+'#')