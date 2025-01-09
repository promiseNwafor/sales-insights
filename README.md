# Sales Insights Dashboard

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Running the ETL Process](#running-the-etl-process)
- [Running the Dash Application](#running-the-dash-application)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)

## Overview
The Sales Insights Dashboard is a data engineering project designed to provide comprehensive insights into customer demographics and sales data. The dashboard focuses on understanding the gender distribution within the customer base and how it influences product purchases. It includes key performance indicators (KPIs) such as total products sold, total sales revenue, and a clear gender split among customers. The dashboard also allows filtering by product category, gender, and date range.

## Features
- **Sales by Gender**: Visualize total products sold and total sales revenue by gender.
- **Sales by Product Category**: Visualize total sales revenue and total products sold by product category.
- **Interactive Filters**: Filter data by product category, gender, and date range.
- **Data Table**: Display raw sales data in a tabular format.

## Technologies Used
- **Python**: Programming language used for data processing and ETL.
- **Pandas**: Library for data manipulation and analysis.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library.
- **Dash**: Web framework for building analytical web applications.
- **PostgreSQL**: Relational database for storing sales data.
- **Gunicorn**: WSGI HTTP server for running the Dash application.

## Project Structure
```
sales-insights/
│
├── etl_process.py          # ETL script for data extraction, transformation, and loading
├── app.py                  # Dash application script
├── requirements.txt        # List of project dependencies
├── Procfile                # Heroku process file
├── retail_sales_dataset.csv # Sample dataset
└── README.md               # Project documentation
```

## Getting Started
### Prerequisites
- **Python 3.7 or higher**
- **PostgreSQL database**

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/promisenwafor/sales-insights.git
    ```
2. Navigate to the project directory:
    ```bash
    cd sales-insights
    ```
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Set up the PostgreSQL database:
    - Create a PostgreSQL database.
    - Update the `DATABASE_URL` in the `etl_process.py` and `app.py` files with your PostgreSQL connection string.

## Running the ETL Process
1. Run the ETL script to extract, transform, and load the data into the PostgreSQL database:
`python etl_process.py`

## Running the Dash Application
1. Run the Dash application:
`python app.py`
2. Open your web browser and navigate to http://127.0.0.1:8050/ to view the dashboard.

## Usage
- **Sales by Gender**: Use the bar chart to compare total products sold and total sales revenue by gender.
- **Sales by Product Category**: Use the bar charts to compare total sales revenue and total products sold by product category.
- **Interactive Filters**: Use the dropdowns and date picker to filter the data displayed in the visualizations and data table.

<img width="1433" alt="Screenshot 2025-01-09 at 04 25 08" src="https://github.com/user-attachments/assets/660ae0fb-3f76-4fcc-9818-03bfa258c0dc" />
<img width="1437" alt="Screenshot 2025-01-09 at 04 24 49" src="https://github.com/user-attachments/assets/5fe38237-58f9-44db-b640-6ccd45a4d131" />


## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact
For any questions or inquiries, please contact admin@misee.pro.
