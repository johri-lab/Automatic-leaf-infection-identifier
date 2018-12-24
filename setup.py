from setuptools import setup, find_packages

requirements = ['numpy', 'matplotlib', 'pandas', 'sklearn', 'opencv-python', 'argparse']

#Description
with open("README.md") as f:
	long_description=f.read()
setup(
    name='Automatic-leaf-infection-identifier ',
    version = '0.1.0',
    author= 'Shikhar Johri',
    author_email= 'shikharjohri123@gmail.com',
    url= 'https://github.com/johri002/Automatic-leaf-infection-identifier',
    long_description long_description,
#Listing Dependencies that it has
    install_requires = requirements
#LICENSE Info
    license= 'LICENSE',
#INFO about where package can run
classifiers=[
'Intended Audience :: Developers',
'License :: OSI Approved :: MIT License',
'Programming Language :: Python :: 2',
'Programming Language :: Python :: 2.7',
'Programming Language :: Python :: 3',
'Programming Language :: Python :: 3.3',
'Operating System :: Windows',
'Operating System :: Linux',
],
#Finding package in a search
   	#keywords='example project'
	#packages=find_packages(exclude=['docs','tests*']
#Shipping extra data with package(that is not a python code)
	#package_data={	
	#'sample':['package_data.dat']
	#}
