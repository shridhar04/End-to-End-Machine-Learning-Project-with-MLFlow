import os
from box.exceptions import BoxValueError
import yaml
from src.mlProject import logger
import json
import joblib
from ensure import ensure_annotation
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotation
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml_file: {path_to_yaml} loaded succesfully")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e    

@ensure_annotation
def create_directories(path_to_directories:list , verbose = True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"ceated directory at: {path}")


@ensure_annotation
def save_json(path:Path , data:Dict):
    with open(path,"w") as f:
        json.dump(data , f , indent = 4)
    logger.info(f"json file saved at: {path} ")    

@ensure_annotation
def load_json(path:Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)

@ensure_annotation
def save_bin(data:Any,path:Path):
    joblib.dump(value=data,filename = path)
    logger.info(f"binary file aved at {path}")
    return data  

@ensure_annotation
def load_bin(path:Path)-> Any:
    data = joblib.load(path)
    logger.info(f"binary file loadef from: {path}")
    return data    

@ensure_annotation
def get_size(path:Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"    
