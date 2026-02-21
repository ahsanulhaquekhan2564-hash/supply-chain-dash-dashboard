import pandas as pd
import plotly.express as px

def get_bottom_warehouse_conclusion(bottom_warehouse, bottom_units):
    """Generates the text conclusion for the dashboard."""
    conclusion = f"The warehouse with the least units sold is **{bottom_warehouse}**, which sold {bottom_units:,.0f} units."
    return conclusion

def Question_4(df_clean: pd.DataFrame):
    """
    Analyzes warehouse performance using a pre-loaded DataFrame.
    """
    
    # Sum units sold per warehouse
    warehouse_totals = df_clean.groupby("warehouse_id")["units_sold"].sum()

    # Find the warehouse with the least units sold
    bottom_warehouse = warehouse_totals.idxmin()   
    bottom_units = warehouse_totals.min()          

    # Prepare data for Plotly
    adjusted_df = warehouse_totals.reset_index()
    adjusted_df.columns = ["Warehouse", "TotalUnitsSold"]
    
    # Create the Plotly bar chart
    fig = px.bar(
        adjusted_df,
        x="Warehouse",
        y="TotalUnitsSold",
        color="TotalUnitsSold",
        color_continuous_scale=px.colors.sequential.Teal,
        title="Units Sold per Warehouse",
        template="plotly_white"
    )

    fig.update_layout(
        xaxis_title="Warehouse",
        yaxis_title="Total Units Sold"
    )

    fig.update_traces(texttemplate='%{y:,.0f}', textposition='outside')
    
    return warehouse_totals, bottom_warehouse, bottom_units, fig