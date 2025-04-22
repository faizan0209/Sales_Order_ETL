import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
import webbrowser
webbrowser.open("http://127.0.0.1:8050/")

# Load data
df = pd.read_csv('files/sales_orders_1000.csv')

# KPIs
total_revenue = df['Total_Price'].sum()
total_orders = len(df)

# Group data
orders_by_month = df.groupby('Month')['Total_Price'].sum().reset_index()
region_data = df['Region'].value_counts().reset_index()
region_data.columns = ['Region', 'Orders']

# Charts
fig1 = px.bar(orders_by_month, x='Month', y='Total_Price', title='Revenue by Month')
fig2 = px.pie(region_data, names='Region', values='Orders', title='Orders by Region')

# Dash App
app = dash.Dash(__name__)
app.title = "Order Dashboard"

app.layout = html.Div([
    html.H1("📊 Order Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Div([
            html.H3("💰 Total Revenue"),
            html.P(f"{total_revenue:,.0f}", style={"fontSize": "24px", "fontWeight": "bold"})
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '20px'}),

        html.Div([
            html.H3("📦 Total Orders"),
            html.P(total_orders, style={"fontSize": "24px", "fontWeight": "bold"})
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '20px'}),
    ]),

    html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
    ]),

    html.H3("🧾 Order Details"),
    dcc.Graph(
        figure=px.scatter(df, x='City', y='Total_Price', hover_data=['Quantity', 'OrderDate'])
    )
])

if __name__ == '__main__':
    app.run(debug=True)

