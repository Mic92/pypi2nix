# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages


setup(
    name="python2nix",
    version="0.0.1",
    author=u"Rok Garbas, Cillian de Róiste",
    description=(
        "Scripts and tools to help create nix package expressions for "
        "python projects"
    ),
    license="GPL",
    keywords="NixOS Nix Packaging",
    url="http://nixos.org",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
    ],
    install_requires=[
        'argh',
        'distlib',
    ],
    entry_points = {
        'console_scripts': [
            'pypi2nix= python2nix.cli:pypi',
        ],
    },
    packages = find_packages(),
)