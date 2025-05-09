from setuptools import setup, find_packages

setup(
    name="hashgrid",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "typer[all]",
        "rich",
        "Pillow",
        "scipy"
    ],
    entry_points={
        "console_scripts": [
            "hashgrid=main:app"
        ]
    },
)