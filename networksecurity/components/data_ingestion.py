"""
Data Ingestion Component

Purpose:
--------
This module implements the Data Ingestion stage of the Machine Learning pipeline.

Pipeline Flow:
--------------
MongoDB Atlas
      ↓
Read Dataset from MongoDB
      ↓
Convert Data into Pandas DataFrame
      ↓
Save Complete Dataset as raw.csv
      ↓
Perform Train-Test Split
      ↓
Save train.csv and test.csv
      ↓
Generate Data Ingestion Artifact

Responsibilities:
-----------------
1. Read data from the MongoDB database.
2. Convert the retrieved documents into a Pandas DataFrame.
3. Save the complete dataset in the Feature Store as raw.csv.
4. Split the dataset into training and testing sets.
5. Save train.csv and test.csv inside the artifact directory.
6. Return a Data Ingestion Artifact containing all generated file paths.

Author: Your Name
"""
