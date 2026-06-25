import os
import sys
import numpy as np
import pandas as pd

# Pipeline Information

PIPELINE_NAME = "network_security"

ARTIFACT_DIR = "artifacts"

# File Names

FILE_NAME = "phisingData.csv"

TRAIN_FILE_NAME = "train.csv"

TEST_FILE_NAME = "test.csv"

# Dataset Information

TARGET_COLUMN = "Result"
 
# Data Ingestion Constants

DATA_INGESTION_DIR_NAME = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"

DATA_INGESTION_INGESTED_DIR = "ingested"

DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2

DATA_INGESTION_COLLECTION_NAME = "NetworkData"

DATA_INGESTION_DATABASE_NAME = "NetworkSecurity"