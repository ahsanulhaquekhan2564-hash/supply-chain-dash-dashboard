import pandas as pd
import plotly.express as px

def plot_average_price_cost(df: pd.DataFrame):


    avg_price = df["unit_price"].mean()
    avg_cost = df["unit_cost"].mean()
    
    df_avg = pd.DataFrame({ "metric": ["Average Unit Price", "Average Unit Cost"],
        "value": [avg_price, avg_cost]
    })


    # Creating the plotly bar chart for Dash
    
    fig = px.bar(
        df_avg,
        x="metric",
        y="value",
        color="value", 
        color_continuous_scale=px.colors.sequential.Teal, 
        labels={"metric": "Metric", "value": "Value"},
        title="RQ1: Average Unit Price vs Average Unit Cost",
        template="plotly_white",
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        margin=dict(l=20, r=20, t=50, b=20),
        yaxis_tickformat='$.2f'
    )

    # Added data labels
    fig.update_traces(texttemplate='$%{y:.2f}', textposition='outside')

    return fig
 