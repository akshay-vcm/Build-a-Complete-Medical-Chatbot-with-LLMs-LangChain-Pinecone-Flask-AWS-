
#it will help to install anykind of folder as local package

from setuptools import find_packages, setup
setup(
    name ="medical_chatbot",
    version="0.1.0",
    author="Akshay Kumar",
    author_email ="akshaykr8747@gmail.com",
    packages=find_packages(),
    install_requires=[]  #it will take all requirements
)








