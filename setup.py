from setuptools import setup, find_packages

setup(
    name="professional-forex-app",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.28.0",
        "pandas>=2.1.0", 
        "numpy>=1.24.0",
        "plotly>=5.15.0",
    ],
)
