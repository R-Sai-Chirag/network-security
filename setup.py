from setuptools import find_packages,setup
from typing import List


def get_requirments()->list[str]:
    requirment_lst:List[str]=[]
    try:
        with open("req.txt","r") as file:
            lines=file.readlines()

            for line in lines:
                requirment=line.strip()
                if requirment and requirment != "-e .":
                    requirment_lst.append(requirment)
    
    
    except FileExistsError:
        print(" req.txt file not found.")

    return requirment_lst

print(get_requirments())


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Sai Chirag",
    author_email="saichirag355@gmail.com",
    packages=find_packages(),
    install_requires=get_requirments()
)
