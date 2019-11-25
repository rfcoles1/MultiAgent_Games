from gym.envs.registration import register

register(
    id='Bees-v0',
    entry_point= 'MultiAgent_Games.Bees.V0.Bees_Environment:BeeEnv',
    max_episode_steps = 50,
)

register(
    id='Bees-v1',
    entry_point= 'MultiAgent_Games.Bees.V1.Bees_Environment:BeeEnv',
    max_episode_steps = 50,
)


