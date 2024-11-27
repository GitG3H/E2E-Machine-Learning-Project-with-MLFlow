## This .py file is used to create folder structure for project.

import os
from pathlib import Path
import logging

#Information level logging with timestamp and error msg are saved in terminal
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') 

project_name= "mlProject"

#__init__.py constructor file to make Python treat directories containing that file as local packages.
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"


]




for filepath in list_of_files:
    filepath = Path(filepath)                           #to automatically convert to windows path (to avoid issues with / \)
    filedir, filename = os.path.split(filepath)         #fielpath destructuring using split function

    #If folder directory is not empty create folder structure and log the info.
    if filedir !="":                                    
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    #If file doesnt exist or if file size is zero, create file and log the info.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")