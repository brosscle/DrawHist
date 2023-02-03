import setuptools

setuptools.setup(
    name="draw-hist",
    version="1.0",
    author="Brossard Clement",
    author_email="",
    description="Draw Histograms and basic statistics from images, ROIs, and colors",
    url="https://github.com/brosscle/DrawHist",
    packages=['DrawHist'],
    package_data={'': ['']},
    scripts=['DrawHist/DrawHist_script.py'],
    entry_points={
        'console_scripts': [
            'draw-hist = DrawHist.console_tool:console_tool',
        ]
    },
    install_requires=[
        'scipy>=1.4.0',
        'numpy>=1.21',
        'nibabel',
        'matplotlib'
    ],
    python_requires='>=3.7',
)
