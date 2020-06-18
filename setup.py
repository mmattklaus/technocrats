import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Technocrats", # Replace with your own username
    version="0.0.1",
    author="Technocrats",
    author_email="technocrats@domain.com",
    description="A temperature and humidity monitoring dashboard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mmattklaus/technocrats",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
