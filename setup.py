import setuptools

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

requires = [
    "pandas >= 0.23.4",
    "xlrd >= 0.9.0",
]

setuptools.setup(
    name="excel_to_dict",
    version="1.0.1",
    author="nixinxin",
    author_email="1025464043@qq.com",
    description="A small package to convert records in excel into dict",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nixinxin/excel_to_dict",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)