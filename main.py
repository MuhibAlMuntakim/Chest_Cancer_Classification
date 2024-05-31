from cnnClassifier import logger
from cnnClassifier.pipeline.Stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.Stage_02_prepare_base_model import PreparingBaseModelPipeline


STAGE_NAME= "Data Ingestion"
try:
        logger.info(f">>>>Stage: {STAGE_NAME} started<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>Stage: {STAGE_NAME} successfully completed<<<<<<<\n\nx===================x ")
        
except Exception as e:
        logger.exception(e)
        raise e 



STAGE_NAME =" Preparing Base Model"
try:
        logger.info(f">>>>Stage: {STAGE_NAME} started<<<<<")
        obj = PreparingBaseModelPipeline()
        obj.main()
        logger.info(f">>>>>Stage:  {STAGE_NAME} successfully completed<<<<<<<\n\nx===================x ")
        
except Exception as e:
        logger.exception(e)
        raise e