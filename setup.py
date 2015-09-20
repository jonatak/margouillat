import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "margouillat",
    version = "0.0.1",
    author = "Jonathan Billaud",
    author_email = "jonathanbillaud@gmail.com",
    description = ("a Rest Api and worker system for ansible"),
    license = "BSD",
    keywords = "ansible flask rest worker",
    packages=['margouillat'],
    long_description=read('README.md'),
    install_requires=[
        'flask',
        'redis'
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
