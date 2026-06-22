"""
setup.py

Purpose:
---------
This file is used to package and distribute the entire Python project.
It contains project metadata (name, version, author, etc.) and tells Python
how to install the project and its dependencies.

Whenever we run:

    pip install -r requirements.txt

and if requirements.txt contains '-e .',
this setup.py file is automatically executed.
"""

# Import setup() and find_packages() from setuptools
# setup() -> Used to configure the project
# find_packages() -> Automatically finds all Python packages
from setuptools import setup, find_packages

# Used for type hinting
from typing import List


# Constant used to identify editable installation
# '-e .' tells pip to install the current project as a package
HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    Reads all dependencies from requirements.txt.

    Parameters
    ----------
    file_path : str
        Path of the requirements.txt file.

    Returns
    -------
    List[str]
        List containing all required Python libraries.
    """

    requirements = []

    try:
        # Open requirements.txt in read mode
        with open(file_path) as file:

            # Read every line
            requirements = file.readlines()

            # Remove newline character (\n) from every package
            requirements = [req.replace("\n", "") for req in requirements]

            # Remove '-e .' because it is not a library.
            # It is only an instruction to execute setup.py
            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)

    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirements


# Project configuration
setup(

    # Project name
    name="network_security",

    # Current version
    version="0.0.1",

    # Author name
    author="Humaima Riaz",

    # Author email
    author_email="",

    # Automatically find all packages
    packages=find_packages(),

    # Install all dependencies from requirements.txt
    install_requires=get_requirements("requirements.txt")
)