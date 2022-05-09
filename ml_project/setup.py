from setuptools import find_packages, setup

from ml_project.utils.read_files import parse_requirements


REQUIREMENTS_PATH = 'requirements.txt'

required_packages = parse_requirements(REQUIREMENTS_PATH)

setup(
    name='ml_project',
    packages=find_packages(),
    version='0.1.0',
    description="MADE ML in Production HW1",
    author="Vyacheslav Yastrebov",
    install_requires=required_packages,
    license="MIT",
)