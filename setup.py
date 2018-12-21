from distutils.core import setup

requirements = ['numpy', 'matplotlib', 'pandas', 'sklearn', 'opencv-python', 'argparse']

setup(
    name='Automatic-leaf-infection-identifier ',
    version = '0.1.0',
    author= 'Shikhar Johri',
    author_email= 'shikharjohri123@gmail.com',
    url= 'https://github.com/johri002/Automatic-leaf-infection-identifier',
    license= 'LICENSE',
    long_description= 'README.md',
    install_requires = requirements
)