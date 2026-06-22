"""
push_data.py

Purpose:
--------
This script implements a simple ETL (Extract, Transform, Load) pipeline.

Pipeline Flow:
--------------
CSV File
    ↓
Read using Pandas
    ↓
Convert DataFrame to JSON Records
    ↓
Connect to MongoDB Atlas
    ↓
Insert Records into MongoDB

Author: Your Name
"""

# Standard Library Imports

import os
import sys
import json

# Third-Party Imports

import certifi
import pandas as pd
import pymongo

from dotenv import load_dotenv


# Project Imports


from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logger

# Load Environment Variables

# Load variables from .env file
load_dotenv()

# Get MongoDB Connection URL
MONGODB_URL = os.getenv("MONGODB_URL")

# SSL Certificate Path
# Used for secure connection with MongoDB Atlas
ca = certifi.where()


class NetworkDataExtract:
    """
    ETL Pipeline Class

    Responsibilities:
    -----------------
    1. Read CSV Dataset
    2. Convert Dataset to JSON
    3. Insert Data into MongoDB
    """

    def __init__(self):
        pass

    # CSV → JSON Conversion

    def csv_to_json_converter(self, file_path: str):
        """
        Reads CSV file and converts every row
        into JSON format.

        Parameters
        ----------
        file_path : str

        Returns
        -------
        list
            List of JSON records.
        """

        try:

            logger.info("Reading CSV file...")

            # Read CSV
            data = pd.read_csv(file_path)

            # Remove unnecessary index
            data.reset_index(drop=True, inplace=True)

            # Convert DataFrame into list of dictionaries
            records = json.loads(
                data.T.to_json()
            ).values()

            logger.info("CSV successfully converted to JSON.")

            return list(records)

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    # Insert Data into MongoDB

    def insert_data_mongodb(
        self,
        records,
        database,
        collection
    ):
        """
        Inserts JSON records into MongoDB.

        Parameters
        ----------
        records : list

        database : str

        collection : str
        """

        try:

            logger.info("Connecting to MongoDB...")

            # Create MongoDB Client
            client = pymongo.MongoClient(
                MONGODB_URL,
                tlsCAFile=ca
            )

            # Select Database
            db = client[database]

            # Select Collection
            collection = db[collection]

            logger.info("Uploading records...")

            # Insert all records
            collection.insert_many(records)

            logger.info("Upload Successful.")

            return len(records)

        except Exception as e:
            raise NetworkSecurityException(e, sys)


# Main Program

if __name__ == "__main__":

    FILE_PATH = "network_data/phisingData.csv"

    DATABASE = "NetworkSecurity"

    COLLECTION = "NetworkData"

    try:

        logger.info("ETL Pipeline Started")

        # Create Object
        network_obj = NetworkDataExtract()

        # CSV → JSON
        records = network_obj.csv_to_json_converter(
            FILE_PATH
        )

        print(f"Total Records : {len(records)}")

        # JSON → MongoDB
        inserted_records = network_obj.insert_data_mongodb(
            records=records,
            database=DATABASE,
            collection=COLLECTION,
        )

        print(
            f"{inserted_records} records inserted successfully."
        )

        logger.info("ETL Pipeline Completed Successfully.")

    except Exception as e:

        logger.exception(e)

        raise NetworkSecurityException(e, sys)