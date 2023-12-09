import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO)

project_name="kafka_Project"

list_of_files=[
    # ".github/workflow/.gitkeep",
    f"notebooks/__init__.py",
    f"notebooks/KafkaConsumer.ipynb",
    f"notebooks/KafkaProducer.ipynb",
]



for filePath in list_of_files:
    filePath=Path(filePath)
    filedir,filename=os.path.split(filePath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir} for file {filename}")
    
    if(not os.path.exists(filePath)) or (os.path.getsize(filePath)==0):
        with open(filePath,"w") as f:
            pass
        logging.info(f"creating empty file : {filePath}")
    else:
        logging.info(f"{filePath} is already exists")
