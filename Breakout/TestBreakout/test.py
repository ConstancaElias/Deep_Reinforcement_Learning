import argparse
import numpy as np
import gym
from environment import Environment


#reference: https://github.com/ShanHaoYu/Deep-Q-Network-Breakout/blob/master/test.py

seed = 11037

def parse():
    parser = argparse.ArgumentParser(description="DQN")
    parser.add_argument('--test_dqn', action='store_true', help='whether test DQN')
    parser.add_argument('--video_dir', default=None, help='output video directory')
    parser.add_argument('--do_render', action='store_true', help='whether render environment')
    try:
        from argument import add_arguments
        parser = add_arguments(parser)
    except:
        pass
    args = parser.parse_args()
    return args


def test(agent, env, total_episodes=30):
    rewards = []
    env.seed(seed)
    for i in range(total_episodes):
        state = env.reset()
        agent.init_game_setting()
        done = False
        episode_reward = 0.0

        #playing one game
        while(not done):
            action = agent.make_action(state, test=True)
            state, reward, done, info = env.step(action)
            episode_reward += reward

        rewards.append(episode_reward)
    print('Run %d episodes'%(total_episodes))
    print('Mean:', np.mean(rewards))


def run(args):
    if args.test_dqn:
        env =  gym.make('BreakoutDeterministic-v4')
        env.reset()
        from qlearn_breakout import playgames
        playGame(args)
        agent = Agent_DQN(env, args)
        test(agent, env, total_episodes=100)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Description of your program')
    parser.add_argument('-m','--mode', help = 'Train / CTrain / Run', required=True)
    args = vars(parser.parse_args())
    
    run(args)