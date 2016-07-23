from setuptools import setup

from pypi2cwl import __version__

setup(name="pypi2cwl",
        version=__version__,
        description='Instrument for extracting tools from PyPi packages and generating CWL tool descriptions',
        author='Anton Khodak',
        author_email='anton.khodak@ukr.net',
        install_requires=[],
        url='https://github.com/common-workflow-language/pypi2cwl',
        packages=["pypi2cwl"],
        entry_points={
            'console_scripts': [
                    'pypi2cwl = pypi2cwl.pypi2cwl:main',
                ]
            },
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Operating System :: OS Independent',
            'Intended Audience :: Developers',
            'Environment :: Console',
            'License :: OSI Approved :: Apache Software License',
            ],
        include_package_data=True,
        )
