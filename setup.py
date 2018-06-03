from setuptools import setup, find_packages

setup(
    name="igamelister",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
        "coloredlogs",
        "lhafile",
        "lxml",
        "requests",
        "progressbar2",
    ],
    entry_points="""
        [console_scripts]
        igamelister=igamelister.__main__:cli
    """,
)
