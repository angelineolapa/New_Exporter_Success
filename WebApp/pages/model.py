#Libraries
import pandas as pd
from dash import html, callback, Input, Output, State, dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

#Own functions
from components.cards.sidemenu import sidemenu_generator
from assets.model.prediction import generate_prediction

#Add alerts to page registry
register_page(__name__, path="/model", name= "Model", 
    title="Tool to predict the success of new Colombian exporters - Prediction Tool", order=3)
    
#Generate side menu
sidemenu = sidemenu_generator()

#Download country data
country_data = pd.read_csv("./data/CountryData.csv")

#Download product classification data
hs_sections = pd.read_csv("./data/hs_sections.csv", usecols=["section", "chapter"], sep=";", encoding = "ISO-8859-1")

##Identify new markets where FTA is available
#Multilateral FTA
can = ["BOL", "ECU", "PER"]
caricom = ["ATG", "BHS", "BRB", "BLZ", "DMA", "GRD", "GUY", "HTI", "JAM", "MSR", "KNA", "LCA", "VCT", "SUR", "TTO"]
efta = ["ISL", "LIE", "NOR", "CHE"]
eu = ["AUT", "BEL", "BGR", "HRV", "CYP", "CZE", "DNK", "EST", "FIN", "FRA", "DEU", "GRC", "HUN", "IRL", "ITA", "LVA", "LTU", "LUX", "MLT", "NLD", "POL", 
      "PRT", "ROU", "SVK", "SVN", "ESP", "SWE"]
mercosur = ["ARG", "BRA", "PRY", "URY"]
pa = ["CHL", "MEX", "PER"]
tri_cent_america = ["GTM", "HND", "SLV"]
#Bilateral fta
bilateral = ["CAN", "CHL","CRI", "CUB", "GBR", "TSR", "KOR", "MEX", "PAN", "USA", "VEN"]
#All FTAs
fta_all = can + caricom + efta + mercosur + eu + pa + tri_cent_america + bilateral

def fta_identifier(market):
    if market in fta_all:
        return 1
    else:
        return 0

#Create form with prediction parameters
year_input = dbc.Row(
    [
        dbc.Label("Year", html_for="model_form_year", width="auto"),
        dbc.Col(
                dbc.Input(id="model_form_year", type="number", placeholder="YY"),
                className="me-3",
            ),
    ],
    className="mb-3",
)

exporter_input = dbc.Row(
    [
        dbc.Label("Exporter Tax Code", html_for="model_form_exporter", width="auto"),
        dbc.Col(
                dbc.Input(id="model_form_exporter", type="text", placeholder="Enter exporter tax code"),
                className="me-3",
            ),
    ],
    className="mb-3",
)

market_input = dbc.Row(
    [
        dbc.Label("Country of Destination *", html_for="model_form_market", width="auto"),
        dbc.Col(
                dbc.Input(id="model_form_market", type="text", placeholder="Enter code of country of destination"),
                className="me-3",
            ),
    ],
    className="mb-3",
)


product_input = dbc.Row(
    [
        dbc.Label("Product **", html_for="model_form_product", width="auto"),
        dbc.Col(
                dbc.Input(id="model_form_product", type="text", placeholder="Enter HS code of product"),
                className="me-3",
            ),
    ],
    className="mb-3",
)

exp_region_input = dbc.Row(
    [
        dbc.Label("Region of Exporter", html_for="model_form_exp_region", width="auto"),
        dbc.Col(
            dbc.RadioItems(
                id="model_form_exp_region",
                options=[
                    {"label": "Región Caribe", "value": "caribe"},
                    {"label": "Región Eje Cafetero y Antioquia", "value": "cafetera"},
                    {"label": "Region Pacífica", "value": "pacifica"},
                    {"label": "Región Central", "value": "central"},
                    {"label": "Región Llanos Orientales/Orinoquia", "value": "llanos"},
                    {"label": "Región Amazonía", "value": "amazónica"},
                ],
            ),
            width=8,
        ),
    ],
    className="mb-3",
)

markets_input = dbc.Row(
    [
        dbc.Label("Other markets of activity", html_for="model_form_markets", width="auto"),
        dbc.Col(
            dbc.Input(id="model_form_markets", type="number", 
            placeholder="Enter no. markets in which exporter is trading"),
        )
    ],
    className="mb-3",
)


products_input = dbc.Row(
    [
        dbc.Label("Other export products", html_for="model_form_products", width="auto"),
        dbc.Col(
            dbc.Input(id="model_form_products", type="number", placeholder="Enter no. products that exporter is trading"),
        )
    ],
    className="mb-3",
)

experience_input = dbc.Row(
    [
        dbc.Label("Years of exporting activity", html_for="model_form_experience", width="auto"),
        dbc.Col(
            dbc.Input(id="model_form_experience", type="number", placeholder="Enter years of exporting activity"),
        )
    ],
    className="mb-3",
)

pnk_input = dbc.Row(
    [
        dbc.Label("Net Weight of Shipment", html_for="model_form_pnk", width="auto"),
            dbc.Col(
                dbc.Input(id="model_form_pnk", type="number", placeholder="Enter net weight in kgs."),
                className="me-3",
            ),
    ],
    className="mb-3",
)

other_exp_input = dbc.Row(
    [
        dbc.Label("Other Expenses", html_for="model_form_other_exp", width="auto"),
            dbc.Col(
                dbc.Input(id="model_form_other_exp", type="number", placeholder="Enter other expenses in USD."),
                className="me-3",
            ),
    ],
    className="mb-3",
)

product_value_input = dbc.Row(
    [
        dbc.Label("Total National Value for HS Code", html_for="model_form_product_value", width="auto"),
            dbc.Col(
                dbc.Input(id="model_form_product_value", type="number", placeholder="Enter total value of exports in previous year"),
                className="me-3",
            ),
    ],
    className="mb-3",
)

form = dbc.Form([year_input, exporter_input, exp_region_input, product_value_input, market_input, product_input, pnk_input, 
        other_exp_input, markets_input, products_input,
        experience_input], id="model_form")

#Generate Card with Prediction Results
results_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H6("Prediction of Success of Exporter with New Product in New Market", className="card-title"),
                html.P("Probability of Success:"),
                dbc.Badge(id="probability_alert", color="Success", className="me-1")
            ]
        ),
    ],
)

#Define layout
layout = html.Div([
    dbc.Row([
        dbc.Col(sidemenu, width=2),
        dbc.Col([
            dbc.Row(form, style={"padding":"20px"}, className="mh-100"),
            dbc.Button("Submit", id="probability_alert_button", class_name="mh-100", n_clicks=0),
        ], width=7),
        dbc.Col([
            dbc.Row([results_card], align="start"),
            dbc.Row(dbc.Badge("Git Hub Repo", href="https://github.com/angelineolapa/New_Exporter_Success", color="primary")),
            dbc.Row(dbc.Badge("*ISO Country Codes", href="https://www.iso.org/obp/ui/#search", color="primary")),
            dbc.Row(dbc.Badge("**Colombian Tariff Schedule (HS Codes)", 
                        href="https://muisca.dian.gov.co/WebArancel/DefMenuConsultas.faces", color="primary")),
        ]),
    ]),
         
]) 

#Callbacks
@callback(
        [Output("probability_alert", "value")], 
        [State("model_form_experience", "value"),
         State("model_form_products", "value"),
         State("model_form_markets", "value"),
         State("model_form_other_exp", "value"),
         State("model_form_pnk", "value"),
         State("model_form_product", "value"),
         State("model_form_market", "value"),
         State("model_form_product_value", "value"),
         State("model_form_exp_region", "value"),
         State("model_form_exporter", "value"),
         State("model_form_year", "value"),
         Input("probability_alert_button", "n_clicks"),
        ], prevent_initial_call=True
    )

def predict(year_selector, exporter_selector, exp_region_selector, product_value_selector, market_selector, product_selector,
    pnk_selector, other_exp_selector, markets_selector, products_selector, experience_selector, n_clicks):

    prod_class = hs_sections[hs_sections["chapter"]==int(product_selector[0:2])]["section"].values[0]

    region = country_data[country_data["market"]==market_selector]["region"].values[0]

    fta = fta_identifier(market_selector)

    overall_exp = markets_selector * products_selector

    results = {"year": year_selector, "exporter":exporter_selector, "exp_region":exp_region_selector, "product_national":product_value_selector, 
        "market":market_selector, "product":product_selector, "pnk":pnk_selector, "other_expenses":other_exp_selector, "active_markets":markets_selector, 
        "active_products":products_selector, "active_years":experience_selector, "prod_class":prod_class,
        "region":region, "fta":fta, "overall_exp":overall_exp}

    if n_clicks is not None:
        new_probability = generate_prediction(results)
        return [str(new_probability)]
    else:
        return ["Please Complete Form and Submit"]
