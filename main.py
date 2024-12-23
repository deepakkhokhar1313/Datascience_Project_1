from src.Datascience_1.logging import logger
from src.Datascience_1.pipeline.data_ingestion_pipeline import (DataIngestionTrainingPipeline)
from src.Datascience_1.pipeline.data_validation_pipeline import (DataValidationTrainingPipeline)

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e