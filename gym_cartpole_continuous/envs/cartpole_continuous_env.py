import math

import numpy as np
from gym import spaces, logger
from gym.envs.classic_control import CartPoleEnv


class CartPoleContinuousEnv(CartPoleEnv):
    def __init__(self):
        super().__init__()

        # direction & scale of force magnitude.
        self.min_action = np.float32(-1.0)
        self.max_action = np.float32(1.0)
        self.action_space = spaces.Box(low=self.min_action, high=self.max_action, shape=(1,), )

    def step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid" % (action, type(action))

        # Discrete Case:(just for reference)
        # force = self.force_mag if action == 1 else -self.force_mag

        # Continuous Case:
        force = self.force_mag * action

        # Note: everything below this is same as gym's cartpole step fun.
        state = self.state
        x, x_dot, theta, theta_dot = state
        costheta = math.cos(theta)
        sintheta = math.sin(theta)
        temp = (force + self.polemass_length * theta_dot * theta_dot * sintheta) / self.total_mass
        thetaacc = (self.gravity * sintheta - costheta * temp) / (
                self.length * (4.0 / 3.0 - self.masspole * costheta * costheta / self.total_mass))
        xacc = temp - self.polemass_length * thetaacc * costheta / self.total_mass
        if self.kinematics_integrator == 'euler':
            x = x + self.tau * x_dot
            x_dot = x_dot + self.tau * xacc
            theta = theta + self.tau * theta_dot
            theta_dot = theta_dot + self.tau * thetaacc
        else:  # semi-implicit euler
            x_dot = x_dot + self.tau * xacc
            x = x + self.tau * x_dot
            theta_dot = theta_dot + self.tau * thetaacc
            theta = theta + self.tau * theta_dot
        self.state = (x, x_dot, theta, theta_dot)
        done = x < -self.x_threshold \
               or x > self.x_threshold \
               or theta < -self.theta_threshold_radians \
               or theta > self.theta_threshold_radians
        done = bool(done)

        if not done:
            reward = 1.0
        elif self.steps_beyond_done is None:
            # Pole just fell!
            self.steps_beyond_done = 0
            reward = 1.0
        else:
            if self.steps_beyond_done == 0:
                logger.warn("You are calling 'step()' even though this environment has already returned done = True."
                            " You should always call 'reset()' once you receive 'done = True' -- any further steps "
                            "are undefined behavior.")
            self.steps_beyond_done += 1
            reward = 0.0

        return np.array(self.state), reward, done, {}
