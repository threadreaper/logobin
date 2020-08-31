#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='logobin',
    version='1.0.3',
    entry_points={
        'console_scripts': [
            'logobin = logobin:main',
        ],
    },
    install_requires=[
        'argparse',
        'pathlib'
    ],
    packages=['logobin'],
    url='https://github.com/threadreaper/8227logo',
    license='Apache License 2.0',
    author='Michael Podrybau',
    author_email='threadreaper@gmail.com',
    description='Command line utility for creating or unpacking boot logos for 8227l-based Android head units',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Natural Language :: English",
        "Intended Audience :: End Users/Desktop",
    ],
    python_requires='>=3.6',
)
