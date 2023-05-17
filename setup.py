from setuptools import setup, find_packages

setup(
    name='convert_RPG_HATPRO_binaries_to_nc',
    version='1.0',
    description="Python package for converting Microwave Radiometer HATPRO binaries to nc",
    long_description='../readme.md',
    # long_description_content_type="text/markdown",
    url='https://github.com/WillyWallace/convert_RPG_HATPRO_binaries_to_nc.git',
    license='MIT',
    author='Andreas Foth',
    author_email='andreas.foth@uni-leipzig.de',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.10',
    install_requires=['numpy', 'xarray', 'setuptools'],
    classifiers=[
        "Development Status :: 1 - Beta",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
    ],
)
