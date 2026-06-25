from datetime import datetime
import os
from networksecurity.constant import training_pipeline


print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)

"""
config_entity.py

Purpose:
--------
This module contains configuration classes used throughout the
Machine Learning pipeline.

Instead of hardcoding file paths, directory names, database names,
and other configuration values inside the pipeline components,
they are organized into reusable configuration objects.

Responsibilities:
-----------------
1. Store the common pipeline configuration.
2. Create a unique artifact directory for every pipeline run.
3. Store Data Ingestion configuration.
4. Generate paths for:
    - Feature Store
    - Raw Dataset
    - Training Dataset
    - Testing Dataset
5. Store MongoDB database and collection information.
6. Provide configuration objects to pipeline components.

"""

class TrainingPipelineConfig:
    """
    Stores common pipeline configuration.
    """

    def __init__(self):

        # Timestamp for every pipeline run
        self.timestamp = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

        # Pipeline Name
        self.pipeline_name = training_pipeline.PIPELINE_NAME

        # Artifact Directory
        self.artifact_dir = os.path.join(
            training_pipeline.ARTIFACT_DIR,
            self.timestamp
        )


class DataIngestionConfig:
    """
    Configuration for Data Ingestion Component.
    """

    def __init__(
        self,
        training_pipeline_config: TrainingPipelineConfig,
    ):

        # Root directory for Data Ingestion
        self.data_ingestion_dir = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME,
        )

        # Feature Store

        self.feature_store_file_path = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,
            training_pipeline.FILE_NAME,
        )

        # Ingested Train File

        self.training_file_path = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR,
            training_pipeline.TRAIN_FILE_NAME,
        )

        # Ingested Test File

        self.testing_file_path = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR,
            training_pipeline.TEST_FILE_NAME,
        )

        # Train Test Split Ratio

        self.train_test_split_ratio = (
            training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        )

        # MongoDB Information

        self.collection_name = (
            training_pipeline.DATA_INGESTION_COLLECTION_NAME
        )

        self.database_name = (
            training_pipeline.DATA_INGESTION_DATABASE_NAME
        )