from setuptools import setup, find_packages
from hhat_jupyter_kernel import version


readme = open("README.md", "r").read()

requirements = open("requirements.txt", "r").readlines()

setup(
    author="Eduardo Maschio",
    python_requires=">=3.8",
    description="A H-hat jupyter kernel.",
    long_description=readme,
    include_package_data=True,
    name="H-hat jupyter kernel",
    packages=find_packages(include=["hhat_jupyter_kernel", "hhat_jupyter_kernel.*"]),
    requires=requirements,
    version=version
)
