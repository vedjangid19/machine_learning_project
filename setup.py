from setuptools import setup, find_packages
from typing import List

# Variable Declaring for set up function
PROJECT_NAME = 'housing-predictor'
VERSION = '0.0.1'
DESCRIPTION = 'This is my first machine learning project end to end.'
AUTHOR = 'Ved Jangid'
PACKAGES = ['housing']
REQUIREMENT_FILE_NAME = 'requirements.txt'

def get_requirement_details()->List[str]:
    """
    Description: This function is going to return list of requirement 
    mention in requirements.txt file

    return This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file
    
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove('-e .')

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    packages=find_packages(),  #PACKAGES,
    install_requires=get_requirement_details()
)