#!/usr/bin/env python
from distutils.core import setup

setup(
    name='pyndm',
    version='1.0.0',
    description='Python Notification Delivery Methods',
    author='Sergey V. Sokolov',
    author_email='sergey.sokolov@air-bit.eu',
    url='https://github.com/sokolovs/pyndm',
    packages=['ndm',],
    install_requires=[
        'requests==2.21.0',
        'smpplib==2.0',
    ],
)
