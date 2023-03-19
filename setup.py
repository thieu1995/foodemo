#!/usr/bin/env python
# Created by "Thieu" at 19:29, 19/03/2023 ----------%
#       Email: nguyenthieu2102@gmail.com            %
#       Github: https://github.com/thieu1995        %
# --------------------------------------------------%

from setuptools import setup
import subprocess
import os

foo_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

if "-" in foo_version:
    # when not on tag, git describe outputs: "1.3.3-22-gdf81228" pip has gotten strict with version numbers so change it to: "1.3.3+22.git.gdf81228"
    # See: https://peps.python.org/pep-0440/#local-version-segments
    v,i,s = foo_version.split("-")
    foo_version = v + "+" + i + ".git." + s

assert "-" not in foo_version
assert "." in foo_version
assert os.path.isfile("foo/version.py")
with open("foo/VERSION", "w", encoding="utf-8") as fh:
    fh.write("%s\n" % foo_version)


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="foodemo3",
    version=foo_version,
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
    package_data={"foo": ["VERSION"]},
    python_requires=">=3.5",
    install_requires=[
        "numpy >= 1.24.2"
    ],
    include_package_data=True,
)
