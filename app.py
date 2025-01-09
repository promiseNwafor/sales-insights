import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import pandas as pd
from sqlalchemy import create_engine

# Connect to PostgreSQL database
DATABASE_URL = 'postgresql://postgres:pzITdqVKbOlhhxCqfxxdxjliSnTgtSAB@autorack.proxy.rlwy.net:43078/railway'
engine = create_engine(DATABASE_URL)

# Fetch data from the database
def fetch_data():
    query = "SELECT * FROM sales_data"
    return pd.read_sql(query, engine)

# Fetch KPI data from the database
def fetch_kpi_data():
    query = "SELECT * FROM kpi_data"
    return pd.read_sql(query, engine)

# Fetch sales by gender and category data from the database
def fetch_sales_by_gender_category():
    query = "SELECT * FROM sales_by_gender_category"
    return pd.read_sql(query, engine)

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the Dash app
app.layout = html.Div([
    html.H1("Sales Dashboard"),
    dcc.Dropdown(
        id='category-filter',
        options=[{'label': cat, 'value': cat} for cat in fetch_data()['Product Category'].unique()],
        placeholder='Select a product category'
    ),
    dcc.Dropdown(
        id='gender-filter',
        options=[{'label': gender, 'value': gender} for gender in fetch_data()['Gender'].unique()],
        placeholder='Select a gender'
    ),
    dcc.DatePickerRange(
        id='date-picker',
        start_date=fetch_data()['Date'].min(),
        end_date=fetch_data()['Date'].max()
    ),
    dcc.Graph(id='sales-graph'),
    dcc.Graph(id='revenue-by-category-graph'),
    dcc.Graph(id='products-sold-by-category-graph'),
    dash_table.DataTable(
        id='sales-table',
        columns=[{"name": i, "id": i} for i in fetch_data().columns],
        data=fetch_data().to_dict('records')
    )
])

# Callback to update the graphs based on filters
@app.callback(
    [Output('sales-graph', 'figure'),
     Output('revenue-by-category-graph', 'figure'),
     Output('products-sold-by-category-graph', 'figure')],
    [Input('category-filter', 'value'),
     Input('gender-filter', 'value'),
     Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date')]
)
def update_graphs(selected_category, selected_gender, start_date, end_date):
    df = fetch_data()
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    if selected_category:
        filtered_df = filtered_df[filtered_df['Product Category'] == selected_category]
    if selected_gender:
        filtered_df = filtered_df[filtered_df['Gender'] == selected_gender]

    # Sales by gender
    sales_by_gender = filtered_df.groupby('Gender').agg({
        'Transaction ID': 'count',
        'Total Amount': 'sum'
    }).rename(columns={'Transaction ID': 'Total Transactions', 'Total Amount': 'Total Sales Revenue'})

    sales_figure = {
        'data': [
            {'x': sales_by_gender.index, 'y': sales_by_gender['Total Transactions'], 'type': 'bar', 'name': 'Total Transactions'},
            {'x': sales_by_gender.index, 'y': sales_by_gender['Total Sales Revenue'], 'type': 'bar', 'name': 'Total Sales Revenue'}
        ],
        'layout': {
            'title': 'Sales by Gender'
        }
    }

    # Revenue by product category
    revenue_by_category = filtered_df.groupby('Product Category').agg({
        'Total Amount': 'sum'
    }).rename(columns={'Total Amount': 'Total Sales Revenue'})

    revenue_by_category_figure = {
        'data': [
            {'x': revenue_by_category.index, 'y': revenue_by_category['Total Sales Revenue'], 'type': 'bar', 'name': 'Total Sales Revenue'}
        ],
        'layout': {
            'title': 'Total Sales Revenue by Product Category'
        }
    }

    # Products sold by product category
    products_sold_by_category = filtered_df.groupby('Product Category').agg({
        'Quantity': 'sum'
    }).rename(columns={'Quantity': 'Total Products Sold'})

    products_sold_by_category_figure = {
        'data': [
            {'x': products_sold_by_category.index, 'y': products_sold_by_category['Total Products Sold'], 'type': 'bar', 'name': 'Total Products Sold'}
        ],
        'layout': {
            'title': 'Total Products Sold by Product Category'
        }
    }

    return sales_figure, revenue_by_category_figure, products_sold_by_category_figure

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)