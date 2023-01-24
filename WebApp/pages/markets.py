#Libraries
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

#Own functions
from components.cards.sidemenu import sidemenu_generator
from assets.graphs.graphs import graph_generator

#Add demographics to page registry
register_page(__name__, path="/markets", name="Markets", 
    title="Tool to predict the success of new Colombian exporters - Markets", order=2)

#Generate side menu
sidemenu = sidemenu_generator()

#Generate figures
markets_region = graph_generator("region")
markets_fta = graph_generator("fta")
markets_gdp = graph_generator("gdp_pc")


#Generate page content
profile1 = dbc.Container([
    dbc.Card([
    dbc.CardBody([
        html.H6("New Markets by World Region", style={"textAlign": "center", "font-weight":"bold"}),
        dbc.Row(dcc.Graph(figure=markets_region, id="markets_region"),justify="center"),
        ])
    ])
])

profile2 = dbc.Container([
    dbc.Card([
    dbc.CardBody([
        html.H6("FTA in New Markets", style={"textAlign": "center", "font-weight":"bold"}),
        dbc.Row(dcc.Graph(figure=markets_fta, id="markets_fta")
            ,justify="center"),
        ])
    ])
])

profile3 = dbc.Container([
    dbc.Card([
    dbc.CardBody([
        html.H6("New Markets by GDP per Capita", style={"textAlign": "center", "font-weight":"bold"}),
        dbc.Row(dcc.Graph(figure=markets_gdp, id="markets_gdp")
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
            dbc.Row(html.H4("Profile of Markets chosen by New Exporters in Colombia (2017-2021)", 
            style={'textAlign': 'center', "font-weight":"bold", "padding":"20px"}, id="subtitle")),  
            dbc.Tabs([
                dbc.Tab(profile1, label="By world region"),           
                dbc.Tab(profile2, label="By FTA"),
                dbc.Tab(profile3, label="By GDP per capita"),
                ]),                                    
        
        ], width=10),
    ],
    align="start",
    justify="between"
    ),            
]
)