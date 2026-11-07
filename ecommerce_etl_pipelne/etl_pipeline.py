# data engineering ->
from pathlib import Path
import sqlite3
import pandas as pd
 
# project folder locations
BASE_DIR= Path(__file__).resolve().parent
print(f"Base Directory: {BASE_DIR}")
 
DATA_DIR=BASE_DIR/"data"
REPORT_DIR=BASE_DIR/"reports"
DATABASE_DIR=BASE_DIR/"database"
 
print(f"Data Directory: {DATA_DIR}")
print(f"Report Directory: {REPORT_DIR}")
print(f"Database Directory: {DATABASE_DIR}")
 
DATABASE_PATH=DATABASE_DIR/"ecommerce_warehouse.db"
print(f"Database Path: {DATABASE_PATH}")
 
# create required folders
def create_folder() -> None:
    """Create report and database folders if they do not exist."""
 
    REPORT_DIR.mkdir(exist_ok=True)
    DATABASE_DIR.mkdir(exist_ok=True)
 
# create_folder() -> creates folder because we called this function
 
# Extract
def extract_data() -> tuple[
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame
]:
    """Read Data from csv files."""
 
    customers=pd.read_csv(DATA_DIR/"customers.csv",encoding="utf-8-sig")
    orders=pd.read_csv(DATA_DIR/"orders.csv",encoding="utf-8-sig")
    deliveries=pd.read_csv(DATA_DIR/"deliveries.csv",encoding="utf-8-sig")
    payments=pd.read_csv(DATA_DIR/"payments.csv",encoding="utf-8-sig")
 
    # clean all columns
    for dataframe in [
        customers,orders,deliveries,payments
    ]:
        dataframe.columns=(
            dataframe.columns.astype(str).str.replace("\ufeff","",regex=False)
            .str.strip()
            .str.lower()
        )
 
    print("Customer columns: ", customers.columns.tolist())
    print("Order columns: ", orders.columns.tolist())
    print("Payment columns: ", payments.columns.tolist())
    print("Delivery columns: ", deliveries.columns.tolist())
 
    return customers,orders,payments,deliveries
extract_data()
 
# transform : clean customer data
def clean_customers(customers: pd.DataFrame) -> pd.DataFrame:
    """Remove Duplicates customers and clean customer fields"""
 
    customers=customers.copy()
 
    customers=customers.drop_duplicates(
        subset=["customer_id"]
    )
 
    customers["customer_name"]=(
        customers["customer_name"].fillna("Unknown Customer")
        .astype(str)
        .str.strip()
        .str.title()
    )
 
    customers["email"]=(
        customers["email"].fillna("unknown@gmail.com")
        .astype(str)
        .str.strip()
        .str.title()
    )
 
    customers["city"]=(
        customers["city"].fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )
 
    return customers
 
# transform : clean deliveries data
def clean_deliveries(deliveries: pd.DataFrame) -> pd.DataFrame:
    """Remove Duplicates customers and clean customer fields"""
 
    deliveries=deliveries.copy()
 
    deliveries=deliveries.drop_duplicates(
        subset=["delivery_id"]
    )
 
    deliveries["delivery_status"]=(
        deliveries["delivery_status"].fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )
 
    deliveries["delivery_city"]=(
        deliveries["delivery_city"].fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )
 
    return deliveries
 
# transform : clean Orders data
def clean_orders(orders: pd.DataFrame) -> pd.DataFrame:
    """Remove Duplicates customers and clean customer fields"""
 
    orders=orders.copy()
 
    orders=orders.drop_duplicates(
        subset=["order_id"]
    )
 
    orders["product_name"]=(
        orders["product_name"].fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )
 
    orders["quantity"]=pd.to_numeric(
        orders["quantity"],
        errors="coerce"
    ).fillna(0)
 
    orders["unit_price"]=pd.to_numeric(
        orders["unit_price"],
        errors="coerce"
    ).fillna(0)
 
    orders["order_date"]=pd.to_datetime(
        orders["order_date"],
        errors="coerce"
    )
 
    orders["total_amount"]=(
        orders["quantity"] * orders["unit_price"]
    )
 
    return orders
 
# transform : clean payments data
def clean_payments(payments: pd.DataFrame) -> pd.DataFrame:
    """Remove Duplicates customers and clean customer fields"""
 
    payments=payments.copy()
 
    payments=payments.drop_duplicates(
        subset=["payment_id"]
    )
 
    payments["product_status"]=(
        payments["product_status"].fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )
 
    payments["payment_method"]=(
        payments["payment_method"].fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )
 
    payments["payment_date"]=pd.to_datetime(
        payments["payment_date"],
        errors="coerce"
    )
 
    return payments


#join all datasets


def join_data(
        customers:pd.DataFrame,
        orders:pd.DataFrame,
        payments:pd.DataFrame,
        deliveries:pd.DataFrame
)-> pd.DataFrame:
    """Join customers,orders ,payments and deliveries."""
    combined_data = orders.merge(
        customers,
        on="customer_id",
        how="left"
    )

    combined_data =combined_data.merge(
            payments,
            on="customer_id",
            how="left"
        )
    combined_data = combined_data.merge(
            deliveries,
            on="customer_id",
            how="left"
        )

    combined_data["customer_name"]={
        combined_data["customer_name"]
        .fillna("Unknown Customer")
    }






