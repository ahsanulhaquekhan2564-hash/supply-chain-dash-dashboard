import pandas as pd

def clean_supply_chain_data(file_path, output_path="cleaned_supply_chain.csv"):
    """
    Loads, cleans, transforms, and saves the supply chain data.
    """
    # 1. Load data
    df_cleaning = pd.read_csv(file_path) 

    # 2. Fill missing values
    df_cleaning = df_cleaning.fillna("Unknown")

    # 3. Handle 'Date' column
    if "Date" in df_cleaning.columns:
        df_cleaning["Date"] = pd.to_datetime(df_cleaning["Date"], errors="coerce")
        
    # 4. Remove duplicates
    df_cleaning = df_cleaning.drop_duplicates() 

    # 5. Rename columns to match what the RQ files expect
    df_cleaning = df_cleaning.rename(columns={
        "SKU_ID": "product_id", 
        "Warehouse_ID": "warehouse_id", 
        "Units_Sold": "units_sold"
    })

    # 6. Change all columns to lowercase  
    df_cleaning.columns = df_cleaning.columns.str.lower()
    
    # 7. Convert core numeric columns
    numeric_cols = ['units_sold', 'unit_price', 'unit_cost', 'promotion_flag']
    for col in numeric_cols:
        if col in df_cleaning.columns:
            df_cleaning[col] = pd.to_numeric(df_cleaning[col], errors='coerce')
    
    # 8. Save
    df_cleaning.to_csv(output_path, index=False)
    return df_cleaning