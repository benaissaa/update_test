

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from setuptools import setup

setup(
    name = 'update_test',
    version='1.0',
    license='GNU General Public License v3',
    author='zouhour ben aissa',
    
    description='HREST API application for Flask',
    package_dir={"update_test": "app_api"},
    
    install_requires=requirements,
    platforms='any',
    install_requires=[
        'flask',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
       
    ],
)