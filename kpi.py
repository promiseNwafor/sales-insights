import pandas as pd
from sqlalchemy import create_engine

def load_data_to_db():
    # # Step 1: Read the dataset
    # file_path = 'retail_sales_dataset.csv'
    # data = pd.read_csv(file_path)

    # # Step 2: Process the data (if needed)
    # # For example, ensure the 'Date' column is in datetime format
    # data['Date'] = pd.to_datetime(data['Date'])

    # # Step 3: Connect to PostgreSQL database
    # DATABASE_URL = 'postgresql://postgres:pzITdqVKbOlhhxCqfxxdxjliSnTgtSAB@autorack.proxy.rlwy.net:43078/railway'  
    # engine = create_engine(DATABASE_URL)

    # # Step 4: Create a table and insert data
    # table_name = 'sales_data'
    # data.to_sql(table_name, engine, if_exists='replace', index=False)

    # print(f"Data successfully inserted into the {table_name} table.")
    
    # Step 1: Read the dataset
    
    file_path = 'retail_sales_dataset.csv'
    data = pd.read_csv(file_path)

    # Step 2: Process the data (if needed)
    # Normalize gender labels
    data['Gender'] = data['Gender'].str.lower()

    # Handle missing values
    data['Gender'].fillna('unknown', inplace=True)
    data['Age'].fillna(data['Age'].median(), inplace=True)
    data['Product Category'].fillna('unknown', inplace=True)
    data['Quantity'].fillna(0, inplace=True)
    data['Price per Unit'].fillna(0, inplace=True)
    data['Total Amount'].fillna(data['Quantity'] * data['Price per Unit'], inplace=True)

    # Ensure the 'Date' column is in datetime format
    data['Date'] = pd.to_datetime(data['Date'])

    # Step 3: Calculate KPIs
    # Total sales revenue
    total_sales_revenue = data['Total Amount'].sum()

    # Total products sold
    total_products_sold = data['Quantity'].sum()

    # Sales by gender and category
    sales_by_gender_category = data.groupby(['Gender', 'Product Category']).agg({
        'Total Amount': 'sum',
        'Quantity': 'sum'
    }).reset_index()

    # Step 4: Connect to PostgreSQL database
    DATABASE_URL = 'postgresql://postgres:pzITdqVKbOlhhxCqfxxdxjliSnTgtSAB@autorack.proxy.rlwy.net:43078/railway'
    engine = create_engine(DATABASE_URL)

    # Step 5: Create tables and insert data
    # Insert raw data
    data.to_sql('sales_data', engine, if_exists='replace', index=False)

    # Insert KPIs
    kpi_data = pd.DataFrame({
        'Total Sales Revenue': [total_sales_revenue],
        'Total Products Sold': [total_products_sold]
    })
    kpi_data.to_sql('kpi_data', engine, if_exists='replace', index=False)

    # Insert sales by gender and category
    sales_by_gender_category.to_sql('sales_by_gender_category', engine, if_exists='replace', index=False)

    print("======= Data successfully transformed and inserted into the database =======")
    
    
load_data_to_db()