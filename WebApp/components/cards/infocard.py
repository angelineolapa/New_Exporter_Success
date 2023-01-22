#Import Libraries
from dash import html
import dash_bootstrap_components as dbc

#Create fuction with layout for infocard
def infocard(text):
    card=dbc.Card([
        dbc.Row([
            dbc.Col([
                dbc.CardBody([
                    html.P(text, className="card_text")
                ],style={"color":"#838383", 'textAlign': 'left'}
                )
            ]),
        ])
    ])
    return card

