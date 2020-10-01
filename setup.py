from setuptools import setup, find_packages

setup(
    name='cfbanking',
    version='1.0.0',
    packages=find_packages(),
    install_requires = [
        'git+https://github.com/theartofcleancode/banking.git@python',
        'git+https://github.com/theartofcleancode/pythonapi.git',
        'git+https://github.com/theartofcleancode/consolefile.git'
    ],
    entry_points={
        'console_scripts': [
            'clean-bank = cfbanking.bank:main'
        ]
    }
)