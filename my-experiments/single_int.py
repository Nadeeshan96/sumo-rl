import gymnasium as gym
import sumo_rl
env = gym.make('sumo-rl-v0',
                net_file="sumo_rl/nets/4x4-Lucas/4x4.net.xml",
                route_file="sumo_rl/nets/4x4-Lucas/4x4c1c2c1c2.rou.xml",
                out_csv_name="outputs/4x4grid/test",
                use_gui=True,
                num_seconds=100000)
obs, info = env.reset()
done = False
while not done:
    next_obs, reward, terminated, truncated, info = env.step(env.action_space.sample())
    done = terminated or truncated