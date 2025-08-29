from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.logging import logger
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
import logging
import sys

# Configure logging so INFO messages appear in console
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

if __name__ == "__main__":
    print("🚀 main.py started")

    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        print("✅ TrainingPipelineConfig created")

        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        print("✅ DataIngestionConfig created")

        dataingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiating data ingestion...")

        dataingestionartifact = dataingestion.initiate_data_ingestion()
        print("📦 Data Ingestion Artifact:", dataingestionartifact)

    except Exception as e:
        print("❌ Error occurred:", e)
        raise NetworkSecurityException(e, sys)
