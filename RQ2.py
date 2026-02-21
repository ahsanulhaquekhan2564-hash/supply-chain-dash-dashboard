import pandas as pd
import plotly.express as px

def get_avg_units_sold_by_region(df: pd.DataFrame):
    """
    Compute average units sold by region - Original Logic
    """
    avg_units = (df.groupby("region")["units_sold"].mean().sort_values(ascending=False).reset_index())

    return avg_units

def plot_avg_units_by_region(df: pd.DataFrame):
    """
    #### Create Plotly bar chart for Dash
    """
    avg_units = get_avg_units_sold_by_region(df)



    # Creating the plotly bar chart for Dash
    
    fig = px.bar(
        avg_units,
        x="region",
        y="units_sold",
        title="Average Units Sold by Region",
        labels={
            "region": "Region",
            "units_sold": "Average Units Sold"
        },
        # Changed the color to Teal gradient (Blue to Green)
        color="units_sold", 
        color_continuous_scale=px.colors.sequential.Teal,
        template="plotly_white"
    )

    fig.update_layout(template="plotly_white")
    
    # Added data labels to show numbers on the bars

    fig.update_traces(texttemplate='%{y:,.2f}', textposition='outside')

    return fig
