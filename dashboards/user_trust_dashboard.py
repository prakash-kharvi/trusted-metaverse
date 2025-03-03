#This script sets up an interactive dashboard using Dash (Plotly) to visualize Trust Scores, User Migration Logs, and Anomaly Detection Alerts.
import dash
import flask
import os
from dash import dcc, html, dash_table
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
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
    migration_data = pd.DataFrame(columns=["Identity verification (I) score", "Asset Ownership (A) score", "behavioral consistency (B) score", "contextual verification (C) score", "Total Trust Score (%)"])

# Create Trust Score Distribution Plot

# Define the bar chart
fig = go.Figure(
    data=[go.Bar(
        x=["Identity verification", "Asset Ownership", "behavioral consistency", "contextual verification"],
        y=[response.json()['Identity verification (I) score'], response.json()['Asset Ownership (A) score'], response.json()['behavioral consistency (B) score'], response.json()["contextual verification (C) score"]],
        marker=dict(color=['lightblue', 'lightgreen', 'orange', 'red'])
    )]
)

# Update layout
fig.update_layout(
    title="",
    xaxis=dict(title="Trust factors"),
    yaxis=dict(title="Trust score (%)", range=[0, 100]),
    plot_bgcolor="#f9f9f9",  # Background inside the plot
    margin=dict(l=60, r=20, t=40, b=60)
)

# Layout of Dashboard
external_css = "dashboards/templates/dashboard.css"
app.layout = html.Div([
    html.Link(rel="stylesheet", href=external_css),

    html.Div(className="dashboard-container", children=[
    html.H2("My Trust Measurement Dashboard"),
    html.Button("User-A Trust score",
            style={
                "backgroundColor": "#dcd3f2",
                "border": "1px solid #ccc",
                "padding": "10px 20px",
                "fontSize": "16px",
                "fontWeight": "bold",
                "borderRadius": "6px",
                "margin": "10px 0",
                "margin-left": "-550px"
            }
        ),
        html.Div(
            dcc.Graph(figure=fig),
            style={"backgroundColor": "#f4f4f4", "padding": "10px", "borderRadius": "8px"}  # Explicitly set background for Graph
        )

    ])
])
# Run App
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
