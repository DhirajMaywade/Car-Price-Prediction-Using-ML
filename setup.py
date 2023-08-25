from setuptools import find_packages,setup

HYPEN_E_FOT='-e.'
def get_requirements(file_path:str):
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("/n","") for req in requirements]

        if HYPEN_E_FOT in requirements:
            requirements.remove(HYPEN_E_FOT)
    
    return requirements


setup(
name='carprice',
author="Dhiraj",
author_email="dhirajmaywade2@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt")
)