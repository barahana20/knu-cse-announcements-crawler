from setuptools import setup, find_packages

install_requires = []
with open('requirements.txt', 'r') as reqs:
  install_requires = reqs.readlines()

setup(
  name='KNU CSE notices crawler',
  version='0.1.0',
  description='KNU CSE notices crawler',
  author='barahana',
  author_email='barahana13@naver.com',
  maintainer='Insik-Won',
  maintainer_email='insikwon@naver.com',
  packages=find_packages('./src'),
  package_dir={'':'src'},
  include_package_data=True,
  install_requires=install_requires,
  entry_points={
    'console_scripts': [
      'comp_crawling = comp_crawling.scripts.comp_crawling:cli'
    ]
  }
)
