from setuptools import setup, find_packages

setup(
    name="bayesian-gbm-parameters-estimator",
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={"": "src"}
)
