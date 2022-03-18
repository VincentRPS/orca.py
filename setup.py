import sys
from setuptools import setup, find_packages

from orca import VERSION

with open("requirements.txt") as f:
    requirements = f.readlines()

with open("README.md") as f:
    readme = f.read()

setup(
    name="orca.py",
    author="b1nzy",
    url="https://github.com/VincentRPS/orca.py",
    version=VERSION,
    packages=find_packages(include=["orca*"]),
    license="MIT",
    description="Pythonic Bot Framework for the orcard API",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    test_suite="tests",
    setup_requires=["pytest-runner==5.3.1"],
    tests_require=[
        "pytest==7.1.1",
        "pytest-benchmark==3.4.1",
        "flake8-tuple==0.4.1",
        "flake8-quotes==3.3.1",
        "flake8-comprehensions==3.8.0",
        "flake8-commas==2.1.0",
        "flake8-builtins==1.5.3",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
