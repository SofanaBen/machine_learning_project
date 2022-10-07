from setuptools import setup
from typing import List

def get_requirements_list()->List[str]:
    """
    This function is going to return a list of requirements mentioned in the 
    requirements.txt file

    """

    with open(EQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readline()

PROJECT_NAME= "housing-predictor"
VERSION = "0.0.1"
AUTHOR_NAME="Sofana Benoutiq"
DESCRIPTION= "This is my first machine learning project that Im trying to create"
PACKAGES=["housing"]
EQUIREMENTS_FILE_NAME= "requirements.txt"

setup(
    name = PROJECT_NAME,
    version= VERSION,
    author= AUTHOR_NAME,
    description= DESCRIPTION,
    packages=PACKAGES,
    install_requires= get_requirements_list()

)
