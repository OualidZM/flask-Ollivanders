import os
from setuptools import setup, find_packages

# from distutils.core import setup, find_packages
with open("README.md", "r") as f:
    description_readme = f.read()

setup(
    name="OllivandersShop",
    version="1.0",
    description="ollivanders application",
    long_description=description_readme,
    long_description_content_type="text/markdown",
    author="Damián Ivanov",
    author_email="bellothornus@gmail.com",
    url="https://www.python.org/sigs/distutils-sig/",
    # packages=["distutils", "controller", "repository", "services", "test"],
    packages=find_packages,
    include_package_data=True,
    license="None",
    classifiers=[
        "Programing Language :: Python :: 3.7.4",
        "License :: None",
        "Operating System :: OS independent",
    ],
    python_requires=">=3.7.4",
)
