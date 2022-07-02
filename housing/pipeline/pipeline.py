from cmath import e
import imp
from tkinter import E
from housing.config.configuration import Configuration
from housing.logger import logging
from housing.exception import HousingException
import os,sys

from housing.component.data_ingestion import DataIngestion
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import DataIngestionConfig

class Pipeline:
    
    def __init__(self,config:Configuration = Configuration()) -> None:
        try:
            self.config = config
            
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(
                data_ingestion_config=self.config.get_data_ingestion_config()
                )
            return data_ingestion.initiate_data_ingestion()
            
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def start_data_validation(self):
        pass
    
    def start_data_transformation(self):
        pass
    
    def start_model_trainer(self):
        pass
    
    def start_model_evaluation(self):
        pass
           
    def start_model_pusher(self):
        pass
    
    def run_pipeline(self):
        try:
            #Data Ingestion
            data_ingestion_config = self.start_data_ingestion()
        except Exception as e:
            raise HousingException(e,sys) from e 