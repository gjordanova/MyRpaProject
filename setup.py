from setuptools import setup, find_packages

setup(
    name="my_rpa_project",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "apache-airflow>=2.10.2",
        "pandas",
        "beautifulsoup4",
        "requests",
    ],
)
