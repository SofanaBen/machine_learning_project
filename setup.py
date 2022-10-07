from setuptools import setup, find_packages
from typing import List 

PROJECT_NAME= "housing-predictor"
VERSION = "0.0.3"
AUTHOR_NAME="Sofana Benoutiq"
DESCRIPTION= "This is my first machine learning project that Im trying to create"
REQUIREMENTS_FILE_NAME= "requirements.txt"

def get_requirements_list()->List[str]:
    """
    This function is going to return a list of requirements mentioned in the 
    requirements.txt file

    """

    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readlines().remove("-e .")

setup(
    name = PROJECT_NAME,
    version= VERSION,
    author= AUTHOR_NAME,
    description= DESCRIPTION,
    packages=find_packages(),
    install_requires= get_requirements_list()

)
