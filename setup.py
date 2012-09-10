from setuptools import setup, find_packages

setup(
    name="tastydocs",
    version="0.1",
    packages = find_packages(),
    package_data={
        'tastydocs' : [
            '*.*',
        ]
    },
    long_description="Automagic web documentation for tastypie REST APIs."
)

