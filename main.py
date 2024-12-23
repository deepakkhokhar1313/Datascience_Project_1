from src.Datascience_1.logging import logger
from src.Datascience_1.pipeline.data_ingestion_pipeline import (DataIngestionTrainingPipeline)

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>> stage {STAGE_NAME} completed <<<")
except Exception as e:
    logger.exception(e)
    raise e