from setuptools import setup, find_packages
import re
import os


cwd = os.path.dirname(os.path.abspath(__file__))


# obtain version
with open(os.path.join(cwd, "screenconnect", "__init__.py")) as f:
    version = re.search(r"__version__\s+=\s+\"(.*)\"", f.read()).group(1)


# obtain long description (readme file)
with open(os.path.join(cwd, "README.md")) as readme_file:
    long_description = readme_file.read()


# obtain requirements
with open(os.path.join(cwd, "requirements.txt")) as reqs_file:
    install_requires = reqs_file.read().splitlines()


setup(
    name="screenconnect",
    version=version,
    url="https://github.com/jacobeturpin/python-screenconnect",
    author="Jacob Turpin",
    packages=find_packages(),
    license="MIT",
    description="A library that provides a Python interface to the ScreenConnect API",
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    install_requires=install_requires,
    python_requires=">=3.5"
)
