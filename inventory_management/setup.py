from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()
setup(
    name="inventory_management",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "setuptools",
    ],
    entry_points={
        "console_scripts": [
            "inventory_management=inventory_management.ui:main",
        ],
    },
    package_data={
        "inventory_management": ["asset/bg.png"],
    },
    long_description=description,
    long_description_content_type="text/markdown",
    
)