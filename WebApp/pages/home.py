#Libraries
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

#Own functions
from components.cards.sidemenu import sidemenu_generator
from assets.graphs.graphs import graph_generator

#Add home to page registry
register_page(__name__, path="/", name="Home", 
    title="Tool to predict the success of new Colombian exporters - Home", order=1)

#Generate side menu
sidemenu = sidemenu_generator()

#Generate graphs
exporter_region = graph_generator("exp_region")
exporter_experience = graph_generator("active_years")
exporter_markets = graph_generator("active_markets")
exporter_products = graph_generator("active_products")

#Generate page content
profile1 = dbc.Container([
    dbc.Card([
    dbc.CardBody([
        html.H6("New Exporter by Region", style={"textAlign": "center", "font-weight":"bold"}),
        dbc.Row(dcc.Graph(figure=exporter_region, id="exporter_region"),justify="center"),
        ])
    ])
])

profile2 = dbc.Container([
    dbc.Card([
    dbc.CardBody([
        html.H6("New Exporter by Experience in Years", style={"textAlign": "center", "font-weight":"bold"}),
        dbc.Row(dcc.Graph(figure=exporter_experience, id="exporter_experience")
            ,justify="center"),
        ])
    ])
])

profile3 = dbc.Container([
    dbc.Card([
    dbc.CardBody([
        html.H6("New Exporter by Active Markets", style={"textAlign": "center", "font-weight":"bold"}),
        dbc.Row(dcc.Graph(figure=exporter_markets, id="exporter_markets")
            ,justify="center"),
        ])
    ])
])

profile4 = dbc.Container([
    dbc.Card([
    dbc.CardBody([
        html.H6("New Exporter by Products Already Traded", style={"textAlign": "center", "font-weight":"bold"}),
        dbc.Row(dcc.Graph(figure=exporter_products, id="exporter_products")
            ,justify="center"),
        ])
    ])
])

#Define layout
layout = html.Div(
[
    dbc.Row(
    [
        dbc.Col(sidemenu, width=2),
        dbc.Col([
            dbc.Row(html.H4("Profile of New Exporters in Colombia (2017-2021)", 
            style={'textAlign': 'center', "font-weight":"bold", "padding":"20px"}, id="subtitle")),  
            dbc.Tabs([
                dbc.Tab(profile1, label="By region"),           
                dbc.Tab(profile2, label="By exerience"),
                dbc.Tab(profile3, label="By markets"),
                dbc.Tab(profile4, label="By products"),
                ]),                                    
        
        ], width=10),
    ],
    align="start",
    justify="between"
    ),            
]
)
