import pandas as pd
import plotly.express as px

def get_rq3_data_and_plot(df: pd.DataFrame):
    """
    RQ3: Identify the top-selling SKU and its regional sales distribution.
    """

    # Total units sold per SKU (simplified)
    sku_totals = df.groupby("product_id")["units_sold"].sum()

    # Top-selling SKU and total units sold
    top_sku = sku_totals.idxmax()
    top_sku_total = sku_totals.max()

    # Regional distribution for the top SKU
    top_sku_regional_sales_df = (
        df[df["product_id"] == top_sku]
        .groupby("region")["units_sold"]
        .sum()
        .reset_index()
        .rename(columns={"units_sold": "top_sku_units_sold"})
    )

    # Conclusion text
    conclusion = (
        f"The top-selling product is *{top_sku}*, "
        f"with a total of {top_sku_total:,.0f} units sold."
    )

    # PLOT CODE 
    fig = px.bar(
        top_sku_regional_sales_df.sort_values('top_sku_units_sold', ascending=False),
        x="region",
        y="top_sku_units_sold",
        title=f"RQ3: Regional Sales Distribution for Top SKU: {top_sku}",
        labels={
            "region": "Region",
            "top_sku_units_sold": "Total Units Sold (Top SKU)"
        },
        color="top_sku_units_sold",
        color_continuous_scale=px.colors.sequential.Teal,
        template="plotly_white"
    )
    fig.update_layout(xaxis_tickangle=-45)
    fig.update_traces(texttemplate='%{y:,.0f}', textposition='outside')
  

    return conclusion, fig


