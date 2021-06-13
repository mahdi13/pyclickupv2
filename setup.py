from setuptools import setup, find_packages

dependencies = [
    'requests',
]

setup(
    name='pyclickupv2',
    version='0.0.1',
    author='mahdi13',
    author_email="mahdi_1373@yahoo.com",
    install_requires=[dependencies],
    packages=find_packages(),
    test_suite="pyclickupv2.tests",
)
