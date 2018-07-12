from setuptools import setup, find_packages

setup(name='pyrl',
      version='0.1',
      description='PyRL is a collection of Python3 scripts for various purposes',
      url='http://github.com/ikoryakovskiy/pyrl',
      author='Ivan Koryakovskiy',
      author_email='i.koryakovskiy@gmail.com',
      license='GNU GPLv3',
      packages=find_packages(),
      install_requires=['numpy'],
      zip_safe=False
)
