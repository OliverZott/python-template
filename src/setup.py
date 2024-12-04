from setuptools import find_packages
from setuptools import setup

setup(
    name="sample_project",
    version="0.8",
    description="Testing installation of Package",
    url="#",
    author="auth",
    author_email="author@email.com",
    license="MIT",
    # packages=["sample_project"],
    packages=find_packages(where="."),
    package_dir={"": "."},
    # install_requires=[
    #     "package1",
    #     "package2",
    # ],
    zip_safe=False,
)
