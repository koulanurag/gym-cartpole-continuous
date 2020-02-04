import gym
import pytest
import gym_cartpole_continuous
from pytest_cases import parametrize_plus, fixture_ref


@pytest.fixture(scope='module')
def env_v0():
    env = gym.make('CartPoleContinuous-v0')
    yield env
    env.close()


@pytest.fixture(scope='module')
def env_v1():
    env = gym.make('CartPoleContinuous-v1')
    yield env
    env.close()


@parametrize_plus('env',
                  [fixture_ref(env_v0),
                   fixture_ref(env_v1)])
def test_continuous_action(env):
    assert isinstance(env.action_space, gym.spaces.Box), 'Action Space should be continuous'

    # step a cont. action in the env.
    env.reset()
    obs, reward, done, info = env.step(env.action_space.sample())

    assert env.observation_space.contains(obs)
