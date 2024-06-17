from setuptools import setup, find_packages

setup(
    name='money-save-preditor',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'pandas',
        'scikit-learn',
        'joblib',
        'numpy',
        'imbalanced-learn',
    ],
)