from setuptools import setup, find_packages

setup(
		name='data_analysis',
		version='0.0.1',
		url='www.github.com/rogerbollmann/data-analysis',
		license='BSD',
		author='Roger Bollmann',
		package=find_packages(),
		install_requires=['PyQT5',
						  'pandas',
						  'sqlalchemy',
						  'nlt',
						  'numpy',
						  'jupyter',
						  'python-twitter'],
		entry_point={},
		extras_require={'dev': ['flake8',]},
		)