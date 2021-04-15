import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="insightlab",
    version="0.4",
    author="IDLab",
    author_email="it-admin@idlab.org",
    description="Library for interacting with Jira Cloud Insight API",
    keywords="insight jira-cloud",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.4",
    url="https://github.com/idlab-org/insightlab",
    packages=["insightlab"],
    classifiers=["Programming Language :: Python :: 3"],
    install_requires=[
        "dotmap>=1.3.23", 
        "requests>=2.25.1",
        "jsonpickle>=2.0.0"
        ],
)
