from setuptools import find_packages, setup


REQUIREMENTS_PATH = 'requirements.txt'


def parse_requirements(requirements_path: str) -> list[str]:
    """Parses pip requirements file
    :param requirements_path: path to requirements file
    :return: list of required packages
    """
    with open(requirements_path) as f:
        requirements_file_lines = f.read().splitlines()
    processed_lines = map(lambda x: x.strip(), requirements_file_lines)
    required_packages = filter(lambda x: x and not x.startswith('#'), processed_lines)
    return list(required_packages)


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