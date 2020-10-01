from setuptools import setup, find_packages

setup(
    name='cfbanking',
    version='1.0.0',
    packages=find_packages(),
    dependency_links = [
        'banking @ git+ssh://github.com/theartofcleancode/banking.git@python#egg=banking-1.0.1',
        'pythonapi @ git+ssh://github.com/theartofcleancode/pythonapi.git#egg=pythonapi-1.0.0',
        'consolefile @ git+ssh://github.com/theartofcleancode/consolefile.git#egg=consolefile-1.0.0'
    ],
    entry_points={
        'console_scripts': [
            'clean-bank = cfbanking.bank:main'
        ]
    }
)