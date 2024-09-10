from setuptools import find_packages,setup
from typing import List


HYPEN_DOT_E = '-e .'
def get_requirements(path:str)->List[str]:
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Mahavir",
    author_email="mrajpurohit1912@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)