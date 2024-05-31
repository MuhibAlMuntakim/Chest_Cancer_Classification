from cnnClassifier import logger
from cnnClassifier.pipeline.Stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.Stage_02_prepare_base_model import PreparingBaseModelPipeline
from cnnClassifier.pipeline.Stage_03_model_trainer import ModelTrainingPipeline


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


STAGE_NAME ="Model Training"
try:
        logger.info(f">>>>Stage: {STAGE_NAME} started<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>Stage:  {STAGE_NAME} successfully completed<<<<<<<\n\nx===================x ")
        
except Exception as e:
        logger.exception(e)
        raise e