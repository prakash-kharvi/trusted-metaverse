#This script sets up an interactive dashboard using Dash (Plotly) to visualize Trust Scores, User Migration Logs, and Anomaly Detection Alerts.
import dash
import flask
import os
from dash import dcc, html, dash_table
import pandas as pd
import plotly.express as px
import requests

# Create a Flask server instance
server = flask.Flask(__name__)

# Initialize Dash App
app = dash.Dash(__name__, server=server)
#server = app.server

# Define a route to serve the CSS file from the "static" folder
@server.route('/dashboards/templates/<path:filename>')
def serve_static(filename):
    return flask.send_from_directory(os.path.join(os.getcwd(), 'dashboards/templates'), filename)

# Fetch User Migration Logs (Assuming API is running on localhost:8000)
API_URL = "http://localhost:8000/compute-trust/"
params = {
    "user_wallet": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
    "virtual_world": "Decentraland"
}
response = requests.get(API_URL, params=params)
if response.status_code == 200:
    migration_data = pd.DataFrame(response.json(), index=[0])  # Convert API response to DataFrame
else:
    migration_data = pd.DataFrame(columns=["user_wallet", "Identity verification (I) score", "Asset Ownership (A) score", "behavioral consistency (B) score", "contextual verification (C) score", "Total Trust Score (%)"])

# Adding a Footer Row
footer_data = {
    "user_wallet": " ",
    "Identity verification (I) score": "wᵢ - 0.4",
    "Asset Ownership (A) score": "wₐ - 0.3",
    "behavioral consistency (B) score": "wᵦ - 0.2",
    "contextual verification (C) score": "w꜀ - 0.1",
}
footer_df = pd.DataFrame(footer_data, index=[0])
full_table_data = pd.concat([migration_data, footer_df],ignore_index=True)

# Layout of Dashboard
external_css = "dashboards/templates/dashboard.css"
app.layout = html.Div([
    html.Link(rel="stylesheet", href=external_css),

    html.Div(className="dashboard-container", children=[
    html.H1("Platform Trust Measurement Dashboard"),
    html.Div("wₓ - weights", className="weights-info"),

    dash_table.DataTable(
        id='user-table',
        columns=[{"name": col, "id": col} for col in full_table_data.columns],
        data=full_table_data.to_dict('records'),
        style_table={'margin': 'auto', 'width': '80%'},
        style_header={
            'backgroundColor': '#f5f3da',
            'fontWeight': 'bold',
            'border': '1px solid black',
            'textAlign': 'center',
            'whiteSpace': 'normal'
        },
        style_data={
            'border': '1px solid black',
            'textAlign': 'center',
            'padding': '10px'
        },
        style_cell={
            'textAlign': 'center',
            'padding': '10px',
            'fontFamily': 'Arial, sans-serif',
            'fontSize': '14px'
        },
        style_data_conditional=[
            {'if': {'row_index': 'even'}, 'backgroundColor': '#f5f3da', 'border': '1px solid black'},  # Zebra striping
            {'if': {'column_id': "Total Trust Score (%)"}, 'fontWeight': 'bold', 'border': '1px solid black'}, # Highlight trust score column
            {'if': {'row_index': len(full_table_data) - 1}, 'border': '0', 'background': '#f4f4f4', 'font-size': '12px', 'color': 'gray', 'margin-top': '10px'}
        ]
    ),

    ])
])
# Run App
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
