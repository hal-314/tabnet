import setuptools

requirements = [
    "scipy>=1.3.0",
    "torch>=1.3.1",
    "numpy>=1.17.2",
    "tqdm>=4.36.1",
    "sklearn>=0.21.0",
    "matplotlib>=3.0.0",
    "IPython",
]

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE",  # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description="long_description",
    long_description_content_type="text/markdown",
    url="https://github.com/hal-314/tabnet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
)
