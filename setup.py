#!/usr/bin/env python
#

import os.path

import setuptools

import sprockets_status


def read_requirements(name):
    requirements = []
    with open(os.path.join('requires', name)) as req_file:
        for line in req_file:
            if '#' in line:
                line = line[:line.index('#')]
            line = line.strip()
            if line.startswith('-r'):
                requirements.extend(read_requirements(line[2:].strip()))
            elif line:
                requirements.append(line)
    return requirements


setuptools.setup(
    name='sprockets-status',
    version=sprockets_status.version,
    description='Application status handler for Tornado',
    long_description='\n' + open('README.rst').read(),
    url='https://github.com/sprockets/sprockets-status',
    license='BSD',
    author='AWeber Communications, Inc.',
    author_email='api@aweber.com',
    packages=['sprockets_status'],
    install_requires=read_requirements('installation.txt'),
    tests_require=read_requirements('testing.txt'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
