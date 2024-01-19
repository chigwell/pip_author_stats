from setuptools import setup, find_packages

setup(
    name='pip_author_stats',
    version='0.0.2',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    description='A tool to generate statistics report for PyPI authors',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/pip_author_stats',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
        'matplotlib',
        'pypistats',
        'bs4',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
