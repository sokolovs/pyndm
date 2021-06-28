#!/usr/bin/env python
from setuptools import setup

setup(
    name='pyndm',
    version='1.0.0',
    description='Python Notification Delivery Methods',
    author='Sergey V. Sokolov',
    author_email='sergey.sokolov@air-bit.eu',
    url='https://github.com/sokolovs/pyndm',
    packages=['ndm'],
    install_requires=[
        'requests==2.25.1',
        'smpplib==2.1.0',
    ],
)
