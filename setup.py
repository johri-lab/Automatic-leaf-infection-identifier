from setuptools import setup, find_packages
from codecs import open
from os import path


dir_path = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(dir_path, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()
	
with open(path.join(dir_path, 'requirements.txt'), encoding='utf-8') as f:
	requirements = f.read().splitlines()

#requirements will now be updated as a list which contains all the dependancies to be installed.

setup(
	name='Automatic-leaf-infection-identifier',
	version = '1.0',
	author= 'Shikhar Johri',
	author_email= 'shikharjohri123@gmail.com',
	url= 'https://johri002.github.io/Automatic-leaf-infection-identifier/',
	description = "The project involves the use of self-designed image processing algorithms and \ntechniques designed using python to segment the disease from the leaf while \nusing the concepts of machine learning to categorise the plant leaves as \nhealthy or infected.",
	long_description = long_description,
#Listing Dependencies that it has
	install_requires = requirements,
#LICENSE Info
	license= 'The MIT License 2018',
#INFO about where package can run
	classifiers=[
	'Intended Audience :: Developers',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 2',
	'Programming Language :: Python :: 2.7',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.3',
	'Programming Language :: Python :: 3.4',
	'Programming Language :: Python :: 3.5',
	'Operating System :: Windows',
	'Operating System :: Linux',
	]
)
