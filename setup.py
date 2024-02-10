#from pip._internal.req.req_install import InstallRequirement
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()   #whenever we pickup every line in requirement it take \n also thats why for avoiding that we do that down function
        requirements=[req.replace("\n","")for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
                
    return requirements
            
setup(
name='mlproject',
version='0.0.1', 
author='Ashutosh',
author_email='ashukanha2000@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')  
    
)