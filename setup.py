from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='sp211_21967646_98',
    version='0.1.1',
    author='Aybuke Kucuk',
    author_email='aaybukekucuk@gmail.com',  
    description='Kısa yol algoritmalarını içeren örnek Python paketi',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aaybukekucuk/sp211_21967646_98',  # GitHub repo adresin
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)