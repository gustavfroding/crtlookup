from setuptools import setup

setup(
    name='crtlookup',
    version='0.1',
    py_modules=['main', 'cli', 'fetch', 'utils'],
    entry_points={
        'console_scripts': [
            'crtlookup = main:run_cli',
        ],
    },
)