# IDS706-Week10-Mini-Project: PySpark Data Processing

This repository contains a PySpark script designed to perform sophisticated data processing on a large dataset, specifically focusing on game statistics. It demonstrates the use of Spark SQL for data querying and DataFrame API for transformations. 

## Project Overview

This PySpark application analyzes a dataset (`games.csv`), performs a column renaming transformation, and then executes a Spark SQL query to filter entries based on a positive ratio threshold. It first transformed the "title" column name to "Game Title" and then did a select query to select all the data entries with positive_ratio >= 90. The output data was exported to the output_data.csv folder with output csv files.

## Prerequisites

Ensure you have the following installed:
- Docker
- Python 3.6 or above
- Apache Spark

## Installation & Running the Project

1. Clone this repository:
    ```
    git clone https://github.com/carolxu369/IDS706-Week10-Mini-Project.git
    ```
2. Install Python dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Run the PySpark script:
    ```
    python data_processing.py
    ```
After running, the script will generate an output_data.csv file in the project directory with the processed data.

Attach the output data screenshot here:
![Output Data](output.png)