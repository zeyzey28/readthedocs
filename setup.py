from setuptools import setup, find_packages

setup(
    name='shortestpath2220674052-docs',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        'sphinx==7.1.2',
        'sphinx-rtd-theme==1.3.0',
        'networkx>=3.0',
        'matplotlib>=3.7.1',
    ],
    extras_require={
        'docs': [
            'sphinx==7.1.2',
            'sphinx-rtd-theme==1.3.0',
        ],
    },
    python_requires='>=3.8',
)