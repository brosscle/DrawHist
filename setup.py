import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DrawHist",
    version="1.0",
    author="Brossard Clement",
    author_email="",
    description="Draw Histograms and basic statistics from images, ROIs, and colors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brosscle/DrawHist",
    packages=['DrawHist'],
    package_data={'': ['']},
    scripts=['DrawHist/DrawHist.py'],
    entry_points={
        'console_scripts': [
            'DrawHist = DrawHist.console_tool:console_tool',
        ]
    },
    install_requires=[
        'scipy>=1.4.0',
        'numpy>=1.21',
        'nibabel',
        'csv',
        'matplotlib'
    ],
    python_requires='>=3.7',
)