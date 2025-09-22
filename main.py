from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.logging import logger
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import (
    DataIngestionConfig,
    TrainingPipelineConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)
import logging
import sys

# Configure logging so INFO messages appear in console
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

if __name__ == "__main__":

    try:
        trainingpipelineconfig = TrainingPipelineConfig()

        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiating data ingestion...")

        dataingestionartifact = dataingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(dataingestionartifact)

        datavalidationconfig = DataValidationConfig(trainingpipelineconfig)
        datavalidation = DataValidation(dataingestionartifact, datavalidationconfig)
        logging.info("Initiating data validation...")

        datavalidationartifact = datavalidation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(datavalidationartifact)

        datatransformationconfig = DataTransformationConfig(trainingpipelineconfig)
        datatransformation = DataTransformation(datavalidationartifact, datatransformationconfig)
        logging.info("Initiating data transformation...")

        datatransformationartifact = datatransformation.intiate_data_transformation()
        logging.info("Data Transformation Completed")
        print(datatransformationartifact)

        logging.info("Model Training sstared")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=datatransformationartifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logging.info("Model Training artifact created")

    except Exception as e:
        raise NetworkSecurityException(e, sys)
