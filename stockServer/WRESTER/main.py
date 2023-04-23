import pandas as pd
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3 import PPO, A2C, DDPG, TD3
from env.StockTradingEnv import StockTradingEnv
from sklearn.model_selection import train_test_split
import time
import warnings
warnings.filterwarnings("ignore")
#import yahoo_fin.stock_info as ya
# Load dataset from yahoo


# Read the data set
train = pd.read_csv('./data/AAPL_train.csv')
# Sort the data by date
train = train.sort_values('Date')
# Train, Test Spilt
# train, test = train_test_split(df, test_size=0.2)
# The algorithms require a vectorized environment to run; Gym environment rendering
env = DummyVecEnv([lambda: StockTradingEnv(train)])
print('Training: Start...')
start_time = time.time()

# Model training
model = PPO('MlpPolicy', env, verbose=1)  # PPO
model.learn(total_timesteps=10000)
end_time = time.time()
print('Training Time: ', end_time - start_time)
print('Training: Done!')

# Read the data set
test = pd.read_csv('./data/AAPL_test.csv')
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

#  https://towardsdatascience.com/creating-a-custom-openai-gym-environment-for-stock-trading-be532be3910e