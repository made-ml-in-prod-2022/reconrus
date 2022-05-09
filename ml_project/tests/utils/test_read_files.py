from textwrap import dedent

import pytest

from ml_project.utils.read_files import parse_requirements


REQUIREMENTS_STR = dedent("""\
    Pillow==8.2.0
    pyparsing==2.4.7
    
    python-dateutil==2.8.1
#    python-slugify==5.0.2
    pytz==2021.1
    PyWavelets==1.1.1
    #PyYAML==5.4.1


    """)

@pytest.fixture()
def requirements_fio(tmpdir):
    fio = tmpdir.join('requirements.txt')
    fio.write(REQUIREMENTS_STR)
    return fio


def test_requirements_parsing(requirements_fio):
    parsed_requirements = parse_requirements(requirements_fio)
    correct_requirements = [
        'Pillow==8.2.0', 'pyparsing==2.4.7', 'python-dateutil==2.8.1', 
        'pytz==2021.1', 'PyWavelets==1.1.1',
    ]

    assert parsed_requirements == correct_requirements
