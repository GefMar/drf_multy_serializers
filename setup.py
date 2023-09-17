from pathlib import Path

from setuptools import find_packages, setup

with Path("README.md").open("r") as fh:
    long_description = fh.read()

description = "Components for creating ViewSets with support for serializers depending on the action and HTTP method."
install_requires = ("djangorestframework>=3.12.4",)

setup(
    name="drf_multy_serializers",
    version="1.0.0",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GefMar/drf_multy_serializers",
    author="Sergei (Gefest) Romanchuk",
    license="MIT",
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10+",
    ],
)
