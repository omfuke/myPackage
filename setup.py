import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="package-om-fuke", # Replace with your own username
    version="0.0.1",

    description="A small example package",
    long_description=long_description,


    packages=setuptools.find_packages(),

    python_requires='>=3.6',
)