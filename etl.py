import logging
import os
import pandas as pd
import sqlalchemy

#  connect to the data warehouse
# db_engine = sqlalchemy.create_engine("postgresql+psycopg2://repl:password@localhost:5432/sales")
# raw_sales_data = pd.read_sql("SELECT * FROM sales", db_engine)

def extract(file_name):
    print(f"Extracting data from {file_name}")
    # pd.read_parquet(file_name)
    return pd.read_csv(file_name)


def transform(data):
    print("Transforming data...")
    # print(data.head())
    # print(data.loc[0])
    # print(data.loc[data['Category Name'] == 'Capsicum', 'Item Name'])
    return data.loc[data['Category Name'] == 'Capsicum']


def load(data):
    print("Loading data...")
    print(data)
    data.to_csv("capsicum.csv", index=False)
    # check that the data is loaded correctly
    file_exists = os.path.exists("capsicum.csv")
    logging.info("Data loaded as CSV: ", file_exists)
    
    
# ELT
# def transform(source_table, target_table):
#   data_warehouse.execute(f"""
#   CREATE TABLE {target_table} AS
#       SELECT
#           CONCAT("Product ID: ", product_id),
#           quantity * price
#       FROM {source_table};
#   """)
    
if __name__ == "__main__":
    data = extract("annex1.csv")
    transformed_data = transform(data)
    load(transformed_data)
    