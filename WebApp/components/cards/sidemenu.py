#Import libraries
import dash_bootstrap_components as dbc

#Own components
from components.cards.sidecard import sidecard
from components.cards.infocard import infocard

#Fuction to create sidemenu
def sidemenu_generator():

    #Side menu cards
    home_card = sidecard("Home", "Profile of New Exporters", "/")
    markets_card = sidecard("Markets", "Profile of New Markets", "/markets")
    model_card = sidecard("Success Predictor", "Success Prediction Tool", "/model")
    
    #Branding row
    info_card = infocard("ML Zoomcamp - Capstone Project", "GitHub Repo", "https://github.com/angelineolapa/New_Exporter_Success")

    #Create sidemenu
    sidemenu = (
        dbc.Row(home_card),
        dbc.Row(markets_card),
        dbc.Row(model_card),
        dbc.Row(info_card),
    )
    return sidemenu