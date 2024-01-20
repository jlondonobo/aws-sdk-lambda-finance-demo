import awswrangler as wr
import pandas as pd
from api import finance


def create_database_if_not_exists(database_name):
    # Check if the database exists
    databases = wr.catalog.get_databases()
    if not any(db["Name"] == database_name for db in databases):
        wr.catalog.create_database(database_name)


def lambda_handler(event, context):
    # Fetch data from the API
    daily_stocks = finance.call_api()

    # Convert the response to a DataFrame
    stocks = pd.DataFrame(daily_stocks)

    # Define your database name
    database_name = "market_tracker"

    # Create the database if it doesn't exist
    create_database_if_not_exists(database_name)

    # Define the S3 path where you want to store the data
    s3_path = "s3://acme/glue/market_tracker/daily_stocks"
    table_name = "daily_stocks"

    # Write the DataFrame to the Glue table, appending to the existing table
    wr.s3.to_parquet(
        df=stocks,
        path=s3_path,
        dataset=True,
        database=database_name,
        table=table_name,
        mode="append"
    )

if __name__ == "__main__":
    lambda_handler(None, None)