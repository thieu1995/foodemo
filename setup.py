#!/usr/bin/env python
# Created by "Thieu" at 19:29, 19/03/2023 ----------%
#       Email: nguyenthieu2102@gmail.com            %
#       Github: https://github.com/thieu1995        %
# --------------------------------------------------%

from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="foodemo3",
    version="0.0.2",
    description="My DEMO project",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/thieu1995/foodemo",
    author="thieu",
    author_email="nguyenthieu2102@gmail.com",
    keywords="libdemo docs api documentation foo python yaml",
    license="MIT",
    packages=["foo"],
    install_requires=[],
    include_package_data=True,
)
