from setuptools import setup, find_packages

setup(
    name="sandbox-env",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests"],
    author="Usman Jalil",
    author_email="ujalil@truemeridian.com",
    description="Python client for sandbox environment",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
