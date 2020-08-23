#!/usr/bin/env python3
from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(name='stringcontext',
      version='1.0.0',
      description='Get the context around an index location in a string',
      long_description=readme,
      long_description_content_type='text/markdown',
      url='https://github.com/wesinator/stringcontext',
      author='wesinator',
      author_email='13hurdw@gmail.com',
      packages=['stringcontext'],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
      ],
      zip_safe=True)
