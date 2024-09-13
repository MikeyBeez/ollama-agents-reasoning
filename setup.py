from setuptools import setup, find_packages

setup(
    name="ollama-agents-reasoning",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "scipy",
        "networkx",
    ],
    author="Mike Bee",
    author_email="mbonsign@gmail.com",
    description="Reasoning and logic functions for Ollama Agents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MikeyBeez/ollama-agents-reasoning",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
