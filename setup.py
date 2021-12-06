from setuptools import setup
setup(
    name='advice-cli',
    version='1.0',
    description='A CLI tool for getting advice from the Advice API',
    author='Ahmed Kira',
    packages=['advice'],
    entry_points={
        'console_scripts': [
            'advice=advice.__main__:main'
        ]
    }
)