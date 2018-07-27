# -*- coding: utf-8 -*-
"""
setup.py: For installing via pip
"""

import io
import os
import re
from setuptools import setup, find_packages


def read(path, encoding='utf-8'):
    path = os.path.join(os.path.dirname(__file__), path)
    with io.open(path, encoding=encoding) as fp:
        return fp.read()


def get_install_requirements(path):
    content = read(path)
    return [
        req
        for req in content.split("\n")
        if req != '' and not req.startswith('#')
    ]



version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('vegasave/save_vega.py').read(),
    re.M
).group(1)

test_requirements=get_install_requirements("requirements_tests.txt")

setup(
    name="vega-save",
    version=version,
    description="Save vega and vega-lite charts locally.",
    author="Syntax Rules",
    author_email="dev@SyntaxRules.com",
    url="https://github.com/SyntaxRules/vega-save",
    license="MIT",
    packages=find_packages(exclude=['docs', 'tests*']),
    package_date={'vegasave': [
        'js/*.js',
        'js/*.html'
    ]},
    install_requires=get_install_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ['vega_save = vegasave.__main__:main']
    },
    test_suite='tests',
    tests_require=test_requirements,
    extras_require={
        'dev': test_requirements,
        'test': test_requirements
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Visualization',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)

