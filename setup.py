from setuptools import setup, find_packages

setup(
    name="hackathon-utils",
    version="0.1",
    packages=find_packages(),
    install_requires=["pandas", "numpy", "matplotlib", "seaborn", "statsmodels"],
    author="Apart Research",
    author_email="sprints@apartresearch.com",
    description="Utilities for running hackathons",
)
