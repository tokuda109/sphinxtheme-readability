# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

version = '0.0.7'
long_description = '\n'.join([
    open(os.path.abspath("./README.rst")).read(),
    open(os.path.abspath("./CHANGES")).read(),
])

setup(
    name='sphinxtheme.readability',
    version=version,
    url='http://sphinxtheme-readability.readthedocs.org/',
    license='BSD',
    author='Tsuyoshi Tokuda',
    author_email='tokuda109@gmail.com',
    description='Sphinx Readability Theme provides a comfortably reading environment for your documentation.',
    long_description=long_description,
    keywords=['Sphinx', 'Readability', 'Theme', 'reStructuredText'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'setuptools',
        'docutils',
        'sphinx',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Processing :: Markup'
    ],
    zip_safe=False,
)
