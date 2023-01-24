#Import Libraries
from dash import html
import dash_bootstrap_components as dbc

#Create fuction with layout for infocard
def infocard(text, linktext, link):
    card=dbc.Card([
        dbc.Row([
            dbc.Col([
                dbc.CardBody([
                    html.P(text, className="card_text"),
                    dbc.CardLink(linktext, href=link)
                ],style={"color":"#838383", 'textAlign': 'left'}
                )
            ]),
        ])
    ])
    return card

