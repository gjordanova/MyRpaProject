
from setuptools import setup, find_packages

setup(
    name="my_rpa_project",
    version="0.1.0",
    description="An RPA project with Airflow DAG, scraping, processing, validating and reporting",
    author="Your Name",
    python_requires=">=3.10",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "apache-airflow>=2.10.2",
        "pandas",
        "numpy",
        "requests",
        "beautifulsoup4",
    ],
)
