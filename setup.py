import os
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="kakaosb",
    version="1.0.0",
    description="kakao i openbuilder skill response template builder ⚒ for python 🐍",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Taemin Lee",
    author_email="persuade@gmail.com",
    python_requires=">=3.6",
    url="https://github.com/taeminlee/kakao-skill-template-builder",
    packages=find_packages(),
    include_package_data=True,
    classifiers=["Programming Language :: Python",],
)