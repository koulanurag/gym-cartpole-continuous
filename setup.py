from os import path
from setuptools import setup

TEST_REQUIRES = ['pytest', 'pytest_cases']
INSTALL_REQUIRES = ['gym']

setup(name='gym-cartpole-continuous',
      version='0.0.1',
      url='https://github.com/koulanurag/gym_cartpole_continuous',
      py_modules=['gym_cartpole_continuous'],
      packages=['gym_cartpole_continuous'],
      author='Anurag Koul',
      author_email='koulanurag@gmail.com',
      description='CartPole environment with continuous action space',
      long_description=open(path.join(path.abspath(path.dirname(__file__)), 'README.md')).read(),
      long_description_content_type='text/markdown',
      license=open(path.join(path.abspath(path.dirname(__file__)), 'LICENSE')).read(),
      install_requires=INSTALL_REQUIRES,
      tests_require=TEST_REQUIRES,
      extras_require={'testing': TEST_REQUIRES},
      python_requires='>=3.5',
      )
