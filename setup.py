from setuptools import find_packages, setup

setup(name='unix-time',
      version='2.0.0',
      url='https://github.com/tallesl/py-unix-time',
      author='Talles Lasmar',
      author_email='talleslasmar@gmail.com',
      description='Unix timestamp made easy.',
      long_description=open('README.md', 'r').read(),
      long_description_content_type='text/markdown',
      packages=find_packages())
