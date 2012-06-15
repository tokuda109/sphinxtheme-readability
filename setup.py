# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='sphinx.themes.readability',
    version='0.0.1',
    url='http://sphinx-themes-readability.readthedocs.org/',
    license='BSD',
    author='Tsuyoshi Tokuda',
    author_email='tokuda109@gmail.com',
    description='',
    long_description='',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'setuptools',
        'docutils',
        'sphinx',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Processing :: Markup'
    ]
    
)
