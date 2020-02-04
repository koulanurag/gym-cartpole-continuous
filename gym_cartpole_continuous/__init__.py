from gym.envs.registration import register

register(
    id='CartPoleContinuous-v0',
    entry_point='gym_cartpole_continuous.envs:CartPoleContinuousEnv',
    max_episode_steps=200,
    reward_threshold=195.0,
)

register(
    id='CartPoleContinuous-v1',
    entry_point='gym_cartpole_continuous.envs:CartPoleContinuousEnv',
    max_episode_steps=500,
    reward_threshold=475.0,
)
