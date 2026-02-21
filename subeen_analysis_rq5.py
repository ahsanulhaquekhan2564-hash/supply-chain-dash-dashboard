import pandas as pd
import plotly.express as px


def promotion_impact_analysis(cleaned_df: pd.DataFrame):
    """
    This will analyze the average units sold with and without promotion and returns a conclusion.
    """
    promotion_unitsold = cleaned_df[cleaned_df['promotion_flag'] == 1]['units_sold'].mean()
    no_promotion_unitsold = cleaned_df[cleaned_df['promotion_flag'] == 0]['units_sold'].mean()

    if promotion_unitsold > no_promotion_unitsold:
        conclusion = "Promotions have increased sales on average."
    elif promotion_unitsold < no_promotion_unitsold:
        conclusion = "Promotions have not increased sales on average (sales were lower)."
    else:
        conclusion = "Promotions appear to have no measurable impact on average sales."
        
    return promotion_unitsold, no_promotion_unitsold, conclusion


def plot_promotion_impact(df_clean: pd.DataFrame):
    """
    Creates a Plotly bar chart visualizing the average units sold during promotion vs non-promotion,
    now including the Teal gradient and data labels.
    """
    # Calculate averages
    promotion_unitsold = df_clean[df_clean['promotion_flag'] == 1]['units_sold'].mean()
    no_promotion_unitsold = df_clean[df_clean['promotion_flag'] == 0]['units_sold'].mean()

    # Prepare dataframe for plotting
    df_plot = pd.DataFrame({
        "Sales Type": ["Promotion", "No Promotion"],
        "Average Units Sold": [promotion_unitsold, no_promotion_unitsold]
    })

    # Create Plotly bar chart
    fig = px.bar(
        df_plot,
        x="Sales Type",
        y="Average Units Sold",
        title="RQ5: Average Units Sold During Promotion vs Non-Promotion",
        color="Average Units Sold", 
        color_continuous_scale=px.colors.sequential.Teal, 
        template="plotly_white"
    )

    fig.update_layout(
        xaxis_title="Sales Type",
        yaxis_title="Average Units Sold"
    )

    # Added data labels 
    # Display the average units sold, rounded to two decimal places. 
    fig.update_traces(texttemplate='%{y:,.2f}', textposition='outside')

    return fig