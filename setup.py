from setuptools import setup, find_packages

setup(
    name="my_library",
    version="0.1.0",
    packages=find_packages(include=["piqe", "piqe.*"])
