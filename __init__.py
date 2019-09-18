from gym.envs.registration import register

register(
    id='Bees-v0',
    entry_point='CoOp_Games.Bees.V0.Bees_Environment:BeeEnv',
    max_episode_steps = 50,
)
