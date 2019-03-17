import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="exm",
    version="0.0.3",
    author="DarkLee",
    author_email="darklee@tenonx.com",
    description="A tool for execution environment management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/darklee/exm.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'exm = exm:main'
        ]
    }
)