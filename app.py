import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd

# Modules for the different parts of the project

import data_modelling_project as dmp
import ahsan_rq1 as vis_rq1
import Baljinder_analysis_rq2 as vis_rq2
import laura_analysis_rq3 as vis_rq3
import Natja_analysis_rq4 as vis_rq4
import subeen_analysis_rq5 as vis_rq5

# Data Preparation 
FILE_PATH = "supply_chain_dataset1.csv"
CLEANED_PATH = "cleaned_supply_chain.csv"

# We clean and load the data first

dmp.clean_supply_chain_data(FILE_PATH, CLEANED_PATH)
df = pd.read_csv(CLEANED_PATH)

######### RQ1 ############
title_rq1 = "RQ1: What is the average unit price and unit cost?"
text_rq1 = "This analysis shows the baseline pricing vs cost strategy."
fig_rq1 = vis_rq1.plot_average_price_cost(df)
rq1_plot_id = "avg-price-cost-plot"

######### RQ2 ############
title_rq2 = "RQ2: Which regions sell the most products on average?"
text_rq2 = "Identifies which regions have the highest average demand."
fig_rq2 = vis_rq2.plot_avg_units_by_region(df)
rq2_plot_id = "avg-units-region-plot"

######### RQ3 ############
title_rq3 = "RQ3: Top-selling SKU and its regional distribution?"
text_rq3, fig_rq3 = vis_rq3.get_rq3_data_and_plot(df)
rq3_plot_id = "top-sku-regional-plot"

######### RQ4 ############
warehouse_totals, bottom_wh, bottom_units, fig_rq4 = vis_rq4.Question_4(df) 
title_rq4 = "RQ4: Which warehouse sells the least products?"
text_rq4 = vis_rq4.get_bottom_warehouse_conclusion(bottom_wh, bottom_units)
rq4_plot_id = "warehouse-sales-plot"

######### RQ5 ############
title_rq5 = "RQ5: What is the impact of promotions on units sold?"
promo_avg, no_promo_avg, conclusion_rq5 = vis_rq5.promotion_impact_analysis(df)
text_rq5 = f"Avg with promotion: {promo_avg:,.2f}. {conclusion_rq5}"
fig_rq5 = vis_rq5.plot_promotion_impact(df)
rq5_plot_id = "promotion-impact-plot"



# Initialize Dash app 

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        # Dashboard Title
        html.H1("Supply Chain Data Analysis Dashboard", className="text-center my-4"),

        # Research Question 1
        dbc.Row(
            dbc.Col(html.H3(title_rq1, className="text-center text-primary"), width=12),
            className="mb-3"
        ),
        dbc.Row(
            dbc.Col(dcc.Markdown(text_rq1, className="text-center lead"), width=12),
            className="mb-4"
        ),
        dbc.Row(
            dbc.Col(dcc.Graph(id=rq1_plot_id, figure=fig_rq1), width=12),
            className="mb-5"
        ),

        # Research Question 2
        dbc.Row(
            dbc.Col(html.H3(title_rq2, className="text-center text-info"), width=12),
            className="mb-3"
        ),
        dbc.Row(
            dbc.Col(dcc.Markdown(text_rq2, className="text-center lead"), width=12),
            className="mb-4"
        ),
        dbc.Row(
            dbc.Col(dcc.Graph(id=rq2_plot_id, figure=fig_rq2), width=12),
            className="mb-5"
        ),

        # Research Question 3
        dbc.Row(
            dbc.Col(html.H3(title_rq3, className="text-center text-warning"), width=12),
            className="mb-3"
        ),
        dbc.Row(
            dbc.Col(dcc.Markdown(text_rq3, className="text-center lead"), width=12),
            className="mb-4"
        ),
        dbc.Row(
            dbc.Col(dcc.Graph(id=rq3_plot_id, figure=fig_rq3), width=12),
            className="mb-5"
        ),

        # Research Question 4
        dbc.Row(
            dbc.Col(html.H3(title_rq4, className="text-center text-danger"), width=12),
            className="mb-3"
        ),
        dbc.Row(
            dbc.Col(dcc.Markdown(text_rq4, className="text-center lead"), width=12),
            className="mb-4"
        ),
        dbc.Row(
            dbc.Col(dcc.Graph(id=rq4_plot_id, figure=fig_rq4), width=12),
            className="mb-5"
        ),

        # Research Question 5
        dbc.Row(
            dbc.Col(html.H3(title_rq5, className="text-center text-success"), width=12),
            className="mb-3"
        ),
        dbc.Row(
            dbc.Col(dcc.Markdown(text_rq5, className="text-center lead"), width=12),
            className="mb-4"
        ),
        dbc.Row(
            dbc.Col(dcc.Graph(id=rq5_plot_id, figure=fig_rq5), width=12),
            className="mb-5"
        ),

    ],
    fluid=True
)

if __name__ == "__main__":
    app.run(debug=True)
