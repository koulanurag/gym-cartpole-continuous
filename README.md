# gym-cartpole-continuous
It's a light wrapper around gym's [CartPole](https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py) env. modified to have continuous action space `(one-line change)`

![Build Status](https://travis-ci.com/koulanurag/gym-cartpole-continuous.svg?branch=master)

## Installation
```bash
cd gym-cartpole-continuous
pip install -e . 
```

## Usage:
```python
>>> import gym
>>> import gym_cartpole_continuous
>>> env = gym.make('CartPoleContinuous-v0')
>>> env.action_space
Box(1,)
>>> env.action_space.sample()
array([0.85574186], dtype=float32)
```

Alternate way to create the environment:
```python
>>> import gym
>>> env = gym.make('gym_cartpole_continuous:CartPoleContinuous-v0')
```

## Env:

|Env|Attributes|
|:----|:----|
|`CartPoleContinuous-v0`| Max Steps: 200|
|`CartPoleContinuous-v1`| Max Steps: 500|
