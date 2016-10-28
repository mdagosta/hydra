#!/usr/bin/env python
from setuptools import setup
setup(
    name = 'hydra',
    version = '0.27',
    author = "Michael D'Agosta",
    author_email = 'mdagosta@codebug.com',
    description = 'Hydra Tornado Utilities',
    url = 'https://github.com/mdagosta/hydra',
    packages = ['hydra'],
    entry_points = {
        "console_scripts": [
            "schema = hydra.schema:main"
            ]
        },
    install_requires = [
        'distribute',
        'tornado == 2.4',
        'py-bcrypt',
        'MySQL-python',
    ],
    )
