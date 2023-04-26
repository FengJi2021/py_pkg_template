from setuptools import setup, find_packages

setup(
    name="pkg_template",
    version="0.1.0",
    description="A simple Python package template",
    author="Feng Ji",
    author_email="tonystarkfcb@gmail.com",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "pkg_template = pkg_template.core:main",
        ]
    },
)
