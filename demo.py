from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
import os,sys
from housing.config.configuration import Configuration

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        # data_validation_config = Configuration().get_data_transformation_config()
        # print(data_validation_config)
    except Exception as e:
        raise HousingException(e,sys) from e
        # logging.error(f"{e}")
        # print(e)
        
if __name__ == "__main__":
    main()