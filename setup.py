import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='stockpy',
    version='0.0.1',
    author='Tom (truedl)',
    author_email='tomten10@gmail.com',
    description='[🤩 Stockpy, offical api wrapper for StockAPI written in Python. 🤩 ]',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/truedl/stockpy',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
