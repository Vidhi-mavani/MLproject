from setuptools import find_packages,setup



setup(
    name='MLproject',
    version= '0.0.1',
    author= 'Vidhi',
    author_email= 'mavanividhi5@gmail.com',
    packages= find_packages(),
    install_requires= ['pandas', 'numpy', 'seaborn'],
)